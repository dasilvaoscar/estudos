const path = require("path");
const express = require("express");
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const PROTO_PATH = path.join(__dirname, "proto", "greeter.proto");
const GRPC_TARGET = process.env.GRPC_TARGET || "localhost:50051";
const HTTP_PORT = process.env.HTTP_PORT || 3000;

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const greeterProto = grpc.loadPackageDefinition(packageDefinition).greeter;

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

const app = express();

app.get("/hello/:name", (req, res) => {
  grpcClient.SayHello({ name: req.params.name }, (err, response) => {
    if (err) {
      console.error("Erro no gRPC:", err.message);
      return res.status(502).json({ error: err.message });
    }
    res.json({
      caller: "node-service (HTTP + gRPC client)",
      grpc_response: response,
    });
  });
});

app.get("/health", (_req, res) => res.json({ status: "ok" }));

app.listen(HTTP_PORT, () => {
  console.log(`API HTTP ouvindo em :${HTTP_PORT}`);
  console.log(`Cliente gRPC apontando para ${GRPC_TARGET}`);
});
