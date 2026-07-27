# Adicionar campo no request e campos `optional`

Base: `HelloRequest { string name = 1; }` (Node = client, Go = server).

## Adicionar um parâmetro no request (aditivo, seguro)

```proto
message HelloRequest {
  string name = 1;
  string language = 2;   // número novo
}
```

Cenários de convivência durante o rollout:

| Client (Node) envia? | Server (Go) conhece? | Resultado |
|---|---|---|
| Não | Não | comportamento antigo |
| **Sim** | **Não** (antigo) | server **ignora** (unknown field). Sem erro, mas valor perdido |
| Não | Sim (novo) | server lê **default** (`""`) — precisa tratar |
| Sim | Sim | funciona pleno |

**Ordem de deploy** (para o parâmetro ter efeito): **servidor (Go) primeiro**
(passa a ler + tratar default), **depois o cliente (Node)** (passa a enviar).

Passos na POC:
1. Editar `.proto` com número novo.
2. Go: rebuild + usar `req.GetLanguage()` tratando `""`.
3. Node: rebuild + passar o campo na chamada.

## Campos opcionais: duas "opcionalidades" no proto3

### 1. Opcionalidade implícita (padrão)
Todo campo singular já é opcional (não existe `required`). Ausente → **valor
default** (`""`, `0`, `false`). **Não dá para distinguir** "não enviado" de
"enviado com default".

### 2. `optional` explícito (presence tracking)
Palavra-chave reintroduzida no protobuf 3.15+. Restaura o `has...()`:

```proto
optional string language = 2;
```

- **Go**: campo vira **ponteiro** (`*string`). `nil` = não setado; `GetLanguage()`
  retorna `""` se nil. Assim `nil` ≠ `""`.
- **Node** (`@grpc/proto-loader` com `oneofs: true`): presença detectável via oneof
  sintético `_language`; ausente vs. `""` distinguíveis.

### Quando usar
| Situação | Escolha |
|---|---|
| Default já serve como "ausente" | implícito |
| Distinguir "não enviado" de "default" | `optional` |
| Bool onde `false` ≠ "não informado" | `optional` |

## Detalhes
- Adicionar/remover `optional` de um campo singular é **wire-compatível** (a
  codificação do campo é idêntica; presença é tratada no código gerado). Recompilar
  os dois lados para expor os acessores.
- `repeated` e `map` **não têm** presença (vazio = ausente); `optional` não se aplica.
- Campos `message` **sempre** têm presença (nil vs. setado).
