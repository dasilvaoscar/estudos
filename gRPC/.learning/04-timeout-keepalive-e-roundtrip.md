# Idle timeout, keepalive e roundtrip

## Roundtrip medido na POC

O `curl` mede o caminho completo `curl → node (HTTP/1.1) → go (gRPC/HTTP/2) → volta`,
em loopback local:

| Chamada | Total | O que pesou |
|---------|-------|-------------|
| **1ª**  | ~42 ms | Inclui abrir a conexão HTTP/2 do Node pro Go (handshake TCP + negociação HTTP/2) |
| 2ª–6ª   | ~5–10 ms | Reusam a conexão gRPC já aberta (novo stream multiplexado) |

A 1ª chamada paga o custo de estabelecer a conexão (`IDLE → CONNECTING → READY`);
as seguintes caem para ~1/5 do tempo. Em rede real, somar a latência de rede.

## Por quanto tempo a conexão fica aberta

Depois de `READY`, ela fica aberta **enquanto houver uso**. O que a fecha é o
**idle timeout** (tempo sem nenhuma chamada ativa):

- **Cliente `@grpc/grpc-js`**: idle timeout padrão de **~30 minutos**. Sem RPC nesse
  período, o channel volta a `IDLE` e fecha o socket; a próxima chamada reabre
  (paga de novo os ~40 ms).
- **Servidor grpc-go**: por padrão **não fecha por inatividade**
  (`MaxConnectionIdle` = infinito, a menos que se configure `keepalive.ServerParameters`).
- **Keepalive pings**: **desligados por padrão** nos dois lados. Sem eles, uma
  conexão ociosa pode "morrer" silenciosamente num NAT/load balancer intermediário
  sem nenhum lado perceber, até a próxima chamada falhar.

## Ajustando o comportamento (channel options no Node)

```js
const grpcClient = new greeterProto.Greeter(
  GRPC_TARGET,
  grpc.credentials.createInsecure(),
  {
    "grpc.client_idle_timeout_ms": 300000,   // fecha após 5 min ocioso
    "grpc.keepalive_time_ms": 10000,         // ping a cada 10s
    "grpc.keepalive_timeout_ms": 5000,       // espera 5s pelo pong
    "grpc.keepalive_permit_without_calls": 1 // pinga mesmo sem RPC ativo
  }
);
```

> ⚠️ Se ligar keepalive agressivo no cliente, configurar o **servidor** para aceitar
> (`EnforcementPolicy.MinTime` no grpc-go), senão o Go derruba a conexão por
> "too many pings".

## Resumo

Conexão persistente e reutilizada; por padrão só fecha após ~30 min ociosa (lado
Node). Os ~40 ms da 1ª chamada só reaparecem após um período ocioso ou se a
conexão cair.
