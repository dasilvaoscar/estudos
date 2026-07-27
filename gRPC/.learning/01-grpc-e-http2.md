# gRPC e HTTP/2 — fundamentos

## O que é gRPC

Framework de RPC (Remote Procedure Call) que permite um serviço chamar métodos
de outro serviço como se fossem funções locais. É **cross-language**: cliente e
servidor podem estar em linguagens diferentes (na POC, Node.js chama Go).

## Contrato via Protocol Buffers (`.proto`)

O contrato é definido num arquivo `.proto` que serve como **fonte única da verdade**
para ambos os lados. Exemplo da POC:

```proto
service Greeter {
  rpc SayHello(HelloRequest) returns (HelloReply);
}

message HelloRequest { string name = 1; }
message HelloReply {
  string message = 1;
  string served_by = 2;
}
```

- Os números (`= 1`, `= 2`) são **field tags** — identificam o campo na
  serialização binária. Não é a ordem, é o identificador; nunca reutilizar um tag.
- A serialização é **binária** (Protobuf), mais compacta e rápida que JSON.

## gRPC roda SEMPRE sobre HTTP/2

Isso é parte da especificação, não é opcional. O HTTP/2 é o que dá ao gRPC:

- **Multiplexação de streams**: várias chamadas na mesma conexão TCP, sem
  head-of-line blocking do HTTP/1.1.
- **Framing binário**: mensagens divididas em frames binários.
- **Compressão de headers (HPACK)**: headers repetidos não trafegam inteiros toda vez.
- **Conexão longa e reutilizável**: em vez de abrir/fechar por requisição.

## Dois caminhos de codegen

Cada linguagem lida com o `.proto` de um jeito:

- **Go**: gera código a partir do `.proto` em **build time** (`protoc` + plugins
  `protoc-gen-go` e `protoc-gen-go-grpc`). Produz `.pb.go` com os tipos e stubs.
- **Node**: pode carregar o `.proto` em **runtime** via `@grpc/proto-loader`,
  dispensando codegen — mais simples para POCs.
