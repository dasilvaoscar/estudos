import { IMessageEvent, w3cwebsocket as WebSocketW3C } from "websocket";
import { createInterface } from "readline";
import { CONFIG, PORT } from "./utils/config";
import { parseMessage } from "./utils/parse";
import { promisify } from "util";

const client = new WebSocketW3C(PORT, CONFIG);
const terminal = createInterface({
  input: process.stdin,
  output: process.stdout,
});

client.onmessage = ReceiveMessage;

function ReceiveMessage(event: IMessageEvent) {
  const message = parseMessage(event.data);
  console.log("\n");
  console.log(message);
}

async function SendMessage() {
  const terminalMessage = promisify(terminal.question).bind(terminal);
  const message = await terminalMessage("\n\nDigite uma mensagem: ");
  client.send(JSON.stringify({ message }));
  SendMessage()
}

SendMessage();
