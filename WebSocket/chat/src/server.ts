import { Server, Socket } from 'socket.io';
import { sessionController } from '@/controllers/SessionController';
import * as types from '@/utils/types';
import { Client } from '@/interfaces/client';
import { configs } from '@/utils/configs';

const eventListener = (socket: Socket) => {
  socket.on(types.CHAT, (data: Client) => {
    sessionController(data, socket);
  });
};

const server = new Server(3000, configs);
server.on(types.OPEN_CONNECTION, eventListener);
