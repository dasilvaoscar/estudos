# Ciclo de vida da conexão gRPC

## A conexão é preguiçosa (lazy)

Criar o client gRPC **não** abre conexão nenhuma. No `node-service/server.js`:

```js
const grpcClient = new greeterProto.Greeter(
  GRPC_TARGET,
  grpc.credentials.createInsecure()
);
```

Isso só cria um **channel** no estado `IDLE`. Nenhum socket TCP/HTTP2 é aberto
quando o server Node sobe.

## Estados do channel

```
new Greeter()        →  IDLE        (nenhum socket aberto)
1ª chamada SayHello  →  CONNECTING → READY   (aí sim abre HTTP/2)
chamadas seguintes   →  READY       (REUSA a mesma conexão)
sem uso por X tempo  →  IDLE        (fecha; reabre na próxima chamada)
```

- **Sobe o Node** → nada conecta no Go.
- **1º `curl /hello/...`** → o channel conecta (`CONNECTING → READY`) e faz o RPC.
- **`curl` seguintes** → reusam a **mesma conexão HTTP/2 persistente** (não reabrem
  por request; apenas abrem um novo *stream* multiplexado).

Essa reutilização é uma das grandes vantagens do gRPC/HTTP/2 sobre o padrão
abrir/fechar por chamada do HTTP/1.1.

## Forçar conexão antecipada (fail-fast no boot)

Se quiser validar na subida que o Go está de pé:

```js
grpcClient.waitForReady(Date.now() + 5000, (err) => {
  if (err) {
    console.error("gRPC não conectou:", err.message);
    process.exit(1);
  }
  console.log("Conexão gRPC pronta com", GRPC_TARGET);
});
```

Ou disparar a conexão sem bloquear:

```js
grpcClient.getChannel().getConnectivityState(true); // o `true` inicia a conexão
```
