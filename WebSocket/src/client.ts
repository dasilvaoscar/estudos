import { randomUUID } from 'crypto';
import { io } from 'socket.io-client';
import * as types from './utils/types';

const SOCKET_SERVER_URL = 'http://localhost:3000';
const client = io(SOCKET_SERVER_URL);

const message = {
  fromUserUUID: randomUUID(),
  toUserUUID: randomUUID(),
  message: 'Hello',
};

const eventListener = (data: any) => {
  message['sessionId'] = data.sessionId;
  console.log(data);
};

setInterval(() => {
  client.emit(types.CHAT, message);
}, 2000);

client.on(types.CHAT, eventListener);
