# Evolução do contrato proto (schema evolution)

## Regra que explica tudo

> A compatibilidade de **wire** do Protobuf é baseada no **número do campo + wire
> type**, **nunca** no nome. O nome só importa para (a) o código gerado e (b) JSON.

## Como o contrato é gerado e consumido na POC (e o risco escondido)

| | Go (server) | Node (client) |
|---|---|---|
| Modelo | codegen em **build time** (`protoc` → `.pb.go`) | **runtime loading** (`@grpc/proto-loader` lê o `.proto` no boot) |
| Binário | "congelado" na versão do proto compilado | lê o `.proto` presente na imagem no boot |
| Mudou o proto? | **recompilar** a imagem | **reiniciar** com o novo `.proto` na imagem |

**Risco estrutural:** cada serviço tem sua **própria cópia** do proto (cada
Dockerfile faz `COPY proto/`). O `proto/greeter.proto` do repo é a fonte da
verdade, mas em runtime cada container carrega um snapshot. Mudar o proto e
rebuildar só um lado faz os contratos **divergirem** silenciosamente.

Mitigação: monorepo com `proto/` compartilhada (POC) → para multi-repo, Buf Schema
Registry / pacote versionado / submodule, com breaking-change detection no CI.

## Caso 1 — Adicionar campo ✅ (seguro)

```proto
message HelloReply {
  string message = 1;
  string served_by = 2;
  int32  request_id = 3;   // número NOVO, nunca usado
}
```

1. Editar `.proto` com número livre.
2. Go: rebuild + preencher no handler.
3. Node: rebuild só se for **ler** o campo.
4. Deploy em qualquer ordem — leitores antigos ignoram campos desconhecidos.

⚠️ Se o campo novo é no **request** e precisa ser usado: deploy **server primeiro**,
depois o client que passa a enviá-lo.

## Caso 2 — Renomear campo ⚠️ (wire-safe, quebra código/JSON)

```proto
string message = 1;   →   string reply_text = 1;   // mesmo número
```

- Wire: **intacto** (número não mudou).
- Quebra: código gerado (acessores Go), consumidores por nome (Node lendo
  `response.message` vira `undefined`), e JSON (usa o nome).

Passos: renomear mantendo o número → atualizar TODO código que usa o nome antigo →
rebuild dos dois.

## Caso 3 — Mudar o número 🚨 (breaking — evitar)

```proto
string message = 1;   →   string message = 7;   // 💥
```

Equivale a remover + adicionar. Dados com o número antigo viram unknown field.
Exige deploy coordenado/simultâneo de todos os lados ou migração com os dois
números coexistindo. Em contrato vivo: **não fazer**. Número é imutável após uso.

## Caso 4 — Remover campo ✅ (com `reserved`)

```proto
message HelloReply {
  reserved 2;
  reserved "served_by";
  string message = 1;
}
```

1. Garantir que nenhum consumidor depende: atualizar **leitores** primeiro, depois
   remover do produtor.
2. Remover e adicionar `reserved <número>;` e `reserved "<nome>";`.
3. Rebuild.

`reserved` impede reuso futuro do número, que causaria corrupção silenciosa.

## Backward vs. forward compatibility

- **Backward**: código novo lê dados de clientes antigos.
- **Forward**: código antigo lê dados de clientes novos (ignora o que não conhece).

| Mudança | Wire ok? | Quebra código/JSON? | Risco |
|---|---|---|---|
| Adicionar (nº novo) | ✅ | não | baixo |
| Renomear (mesmo nº) | ✅ | sim | médio |
| Mudar número | ❌ | sim | alto |
| Remover (com `reserved`) | ✅ | consumidores do campo | médio |
| Mudar tipo | depende | depende | ver abaixo |

**Mudar tipo:** compatíveis — `int32`/`int64`/`uint32`/`uint64`/`bool` (varint);
`sint32`↔`sint64`; `string`↔`bytes` (se UTF-8 válido). Entre grupos diferentes
(ex.: `int32`→`string`) **corrompe**. `singular`↔`repeated` é breaking.

## Boas práticas

- Tratar `.proto` como API pública versionada.
- Breaking-change detection no CI (`buf breaking`).
- Reservar tags 1–15 para campos quentes (1 byte de overhead na tag).
- Nunca reaproveitar números; usar `reserved` ao remover.
