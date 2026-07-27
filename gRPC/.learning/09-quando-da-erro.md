# Quando uma mudança de contrato REALMENTE dá erro

Muita mudança é silenciosa (ignorada/default). Mas há casos que erram de verdade.
Separar por **quando** o erro aparece.

## 1. Build/boot (antes de qualquer chamada)
- **Proto malformado / número duplicado**: Node (`@grpc/proto-loader` faz `loadSync`
  no boot) **não sobe**; Go **não builda** (`protoc` falha). Falha cedo e barulhento.

## 2. Decode no wire (runtime) 🚨
Wire casa por **número + wire type**. Mudar o tipo para um **wire type incompatível**
mantendo o número corrompe a leitura:

```proto
string language = 2;   →   int32 language = 2;   // len-delimited (2) → varint (0)
```

Resultado: corrupção silenciosa ou **parse error** (`INTERNAL`, "cannot parse
invalid wire-format data"). É o motivo de `reserved` existir.

> Trocas no mesmo grupo (`int32`↔`int64`, `string`↔`bytes`) **não** erram. O
> problema é atravessar grupos de wire type.

## 3. Método não encontrado → `UNIMPLEMENTED` (code 12)
Roteamento é pela path qualificada: `/greeter.Greeter/SayHello` (`package` +
`service` + `rpc`). Mudar **qualquer parte** só de um lado → cliente antigo recebe
`UNIMPLEMENTED`:
- renomear o método, o `service`, o `package`, ou remover o método.

Contraste: renomear **campo** é wire-safe; renomear **método/serviço/package** é
breaking com erro na cara do cliente.

## 4. Payload grande → `RESOURCE_EXHAUSTED`
Limite default de mensagem (~4 MB) no receptor. Campos/`repeated` que cresçam além
disso → `RESOURCE_EXHAUSTED` ("Received message larger than max"). Ajustável via
`grpc.max_receive_message_length`.

## 5. proto2 `required` (n/a na POC)
Em proto2, `required` ausente = parse error. proto3 removeu `required` por isso —
campo ausente vira default, nunca erro. "Campo obrigatório" não existe em proto3.

## 6. Erro de aplicação (não é do protobuf)
Server lê default (`name = ""` de cliente antigo) e a lógica de negócio rejeita →
você retorna erro (ex.: `INVALID_ARGUMENT`). É onde a compatibilidade silenciosa
vira erro visível se o default não for tratado.

## Tabela-resumo

| Situação | Dá erro? | Onde/qual |
|---|---|---|
| Adicionar campo (nº novo) | não | default/ignorado |
| Renomear campo (mesmo nº) | não no wire | quebra código gerado |
| Renomear método/serviço/package | **sim** | `UNIMPLEMENTED` no client |
| Mudar tipo p/ wire incompatível | **sim** | parse error / corrupção |
| Reusar número removido | **sim** | corrupção — use `reserved` |
| Payload > ~4 MB | **sim** | `RESOURCE_EXHAUSTED` |
| Proto malformado | **sim** | Node não sobe / Go não builda |
| Default cai na regra de negócio | **sim** (seu código) | ex.: `INVALID_ARGUMENT` |

**Resumo:** mudanças aditivas em campos raramente erram. Erram de verdade: mexer na
**identidade do RPC** (`UNIMPLEMENTED`), **atravessar wire types** (parse error),
**reusar números** (corrupção) e **estourar o tamanho** (`RESOURCE_EXHAUSTED`).
