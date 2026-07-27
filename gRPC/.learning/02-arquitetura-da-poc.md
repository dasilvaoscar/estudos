# Arquitetura da POC

## Visão geral

Duas APIs simples que se comunicam via gRPC, orquestradas com docker-compose:

- **go-service**: servidor gRPC em Go (porta `50051`)
- **node-service**: API HTTP em Node.js que atua como cliente gRPC (porta `3000`)

```
  HTTP request                gRPC call
Cliente ────────▶ node-service ────────▶ go-service
  (curl)          (Express + client)     (gRPC server)
```

O `node-service` é a **borda** (fala REST/JSON com o mundo) e o `go-service` é um
serviço interno acessado só via gRPC.

## Estrutura de arquivos

```
proto/greeter.proto     Contrato compartilhado (fonte da verdade)
go-service/             Servidor gRPC (Go)
  ├── go.mod
  ├── main.go
  └── Dockerfile        Gera o .pb.go durante o build (protoc)
node-service/           API HTTP + cliente gRPC (Node)
  ├── package.json
  ├── server.js         Carrega o .proto em runtime
  └── Dockerfile
docker-compose.yml
```

## Decisões importantes

### Contexto de build na raiz
Ambos os serviços precisam da pasta `proto/`, então no `docker-compose.yml` o
`build.context` é a raiz do projeto (`.`) e cada serviço aponta seu
`dockerfile`. Assim os dois Dockerfiles copiam `proto/` do mesmo lugar.

### Go gera o código no build
Não versionamos `.pb.go`. O Dockerfile do Go instala `protoc` + plugins, roda o
codegen e faz `go mod tidy` para resolver o `go.sum` (que não existia no repo).

### Comunicação entre containers por nome de serviço
O `node-service` acha o Go via `GRPC_TARGET=go-service:50051` — o Docker Compose
resolve `go-service` pelo DNS interno da rede do compose.

## Rodar e testar

```bash
docker compose up --build
curl http://localhost:3000/hello/Oscar
```

Resposta:

```json
{
  "caller": "node-service (HTTP + gRPC client)",
  "grpc_response": {
    "message": "Olá, Oscar!",
    "served_by": "go-service (gRPC server)"
  }
}
```

## Armadilha observada: RTK sumariza saída de `curl`

No terminal, a saída JSON do `curl` apareceu "esquematizada" (só os tipos:
`{ caller: string, ... }`) por causa do proxy RTK que economiza tokens. A resposta
real está correta — para ver o corpo bruto, salvar num arquivo e ler o arquivo.
