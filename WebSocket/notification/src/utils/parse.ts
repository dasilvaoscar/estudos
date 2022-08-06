import { RawData } from "ws";

export const parseMessage = (message: RawData | Buffer | string): object =>
  JSON.parse(message.toString());