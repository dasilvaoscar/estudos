# Tipos de RPC: unary vs. streaming

## O que a POC usa: unary (request-response)

O contrato em `proto/greeter.proto`:

```proto
rpc SayHello(HelloRequest) returns (HelloReply);
```

Sem `stream` em nenhum lado → **uma requisição, uma resposta**. O Node manda um
`HelloRequest`, o Go devolve um `HelloReply`, e o RPC termina. Conceitualmente
equivale a uma chamada REST comum.

## Os 4 tipos que o gRPC oferece

| Tipo | Proto | Fluxo | Uso típico |
|------|-------|-------|-----------|
| **Unary** (o nosso) | `rpc M(Req) returns (Resp)` | 1 req → 1 resp | CRUD, consultas simples |
| **Server streaming** | `rpc M(Req) returns (stream Resp)` | 1 req → N resp | feed de eventos, download em chunks |
| **Client streaming** | `rpc M(stream Req) returns (Resp)` | N req → 1 resp | upload em chunks, agregação |
| **Bidirectional** | `rpc M(stream Req) returns (stream Resp)` | N req ↔ N resp | chat, telemetria em tempo real |

## Distinção importante: padrão do RPC vs. conexão de transporte

São dois níveis diferentes — fácil de confundir:

- **Padrão do RPC** = unary (request-response). Cada `curl /hello/...` é uma chamada
  independente que começa e termina.
- **Conexão de transporte** = HTTP/2 **persistente e multiplexada**. Mesmo cada RPC
  sendo unary, todos trafegam pela **mesma conexão reaproveitada** (ver roundtrip
  em [04-timeout-keepalive-e-roundtrip.md](./04-timeout-keepalive-e-roundtrip.md):
  1ª chamada ~42ms abrindo, seguintes ~5–10ms reusando).

Ou seja: a *forma* é request-response, mas roda sobre uma conexão longa — não é
"abre e fecha" por chamada como o HTTP/1.1 costuma ser.
