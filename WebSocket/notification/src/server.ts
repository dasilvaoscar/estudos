import { WebSocket, RawData, Server as WebSocketServer } from "ws";
import { parseMessage } from "./utils/parse";

const websocket = new WebSocketServer({ port: 5000 });

websocket.on("connection", (ws) => {
  ws.on("message", (event) => onMessage(event, ws));
  ws.on("close", () => console.log("Connection closed"));
  ws.on("error", (error) => console.log(error));
});

function onMessage(event: RawData, ws: WebSocket) {
  const message = parseMessage(event);
  console.log(message);
  ws.send(JSON.stringify({ message: "Resposta do servidor" }));
}
