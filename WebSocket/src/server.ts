import { Server } from 'socket.io';
import { IMessage } from './core/domains/message';
import * as types from './utils/types';

const server = new Server(3000);

const eventListener = (data: IMessage) => {
  const message = `${data.message} from ${data.userUUID}`;
  console.log(message);
};

server.on('connection', (socket) => {
  socket.on(types.EVENT, eventListener);
});
