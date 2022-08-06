import { w3cwebsocket as WebSocket } from "websocket";
import { parseMessage } from "./parse";

const client = new WebSocket("ws://localhost:5000/", "echo-protocol");

client.onopen = () => {
  if (client.readyState === client.OPEN) {
    setInterval(
      () => client.send(JSON.stringify({ message: "Message" })),
      1000
    );
  }
};

client.onmessage = (event) => console.log(parseMessage(event.data));
