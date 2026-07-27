# POC gRPC: Node.js + Go

POC de duas APIs simples que se comunicam via **gRPC**:

- **go-service**: servidor gRPC em Go (porta `50051`)
- **node-service**: API HTTP em Node.js que atua como cliente gRPC (porta `3000`)

```
  HTTP request                gRPC call
Cliente ────────▶ node-service ────────▶ go-service
  (curl)          (Express + client)     (gRPC server)
```

## Estrutura

```
proto/greeter.proto     Contrato compartilhado entre os serviços
go-service/             Servidor gRPC (Go) — codegen do proto no build
node-service/           API HTTP + cliente gRPC (Node) — carrega o proto em runtime
docker-compose.yml
```

## Como rodar

```bash
docker compose up --build
```

## Testar

```bash
curl http://localhost:3000/hello/Oscar
```

Resposta esperada:

```json
{
  "caller": "node-service (HTTP + gRPC client)",
  "grpc_response": {
    "message": "Olá, Oscar!",
    "served_by": "go-service (gRPC server)"
  }
}
```

Health check:

```bash
curl http://localhost:3000/health
```

## Notas técnicas

- O **Go** gera o código do protobuf durante o build da imagem (`protoc` + plugins),
  então não há arquivos `.pb.go` versionados.
- O **Node** carrega o `.proto` dinamicamente em runtime via `@grpc/proto-loader`,
  dispensando codegen.
- Ambos compartilham o mesmo `proto/greeter.proto` como fonte da verdade do contrato.
