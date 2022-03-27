import { io } from 'socket.io-client';
import { IMessage } from './core/domains/message';
import * as types from './utils/types';

const SOCKET_SERVER_URL = 'http://localhost:3000';
const client = io(SOCKET_SERVER_URL);

const eventListener = (data: any) => {
  console.log(data);
};

const message: IMessage = {
  userUUID: '12334',
  message: 'Hello',
};

client.emit(types.CHAT, message);

client.on(types.CHAT, eventListener);
