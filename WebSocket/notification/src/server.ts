import { Server as WebSocketServer } from "ws";
import { parseMessage } from "./parse";

const websocket = new WebSocketServer({ port: 5000 });

websocket.on("connection", (ws) => {
  ws.on("message", (event) => {
    const message = parseMessage(event);
    console.log(message);
    ws.send(JSON.stringify({ message: "Response" }));
  });
});
