import { Server, Socket } from 'socket.io';
import { Session } from './core/domains/session';
import { Message } from './core/domains/message';
import { SessionUseCase } from './core/useCases/session.useCase';
import * as types from './utils/types';

const configs = {
  cors: {
    origin: '*',
  },
};

export interface Client {
  sessionId?: string;
  fromUserUUID: string;
  toUserUUID: string;
  message: string;
}

const server = new Server(3000, configs);

const sessionUseCase = new SessionUseCase();

const sessionController = (data: Client, socket: Socket) => {
  const session: Session =
    data.sessionId === undefined
      ? sessionUseCase.createSession({
          fromUserUUID: data.fromUserUUID,
          toUserUUID: data.toUserUUID,
        })
      : sessionUseCase.getSession(data.sessionId);

  const message = new Message({
    message: data.message,
    userUUID: data.fromUserUUID,
  });

  socket.emit(types.CHAT, {
    sessionId: session.id,
    message: message.message,
    userUUID: message.userUUID,
  });

  session.addMessage(message);
};

const eventListener = (socket: Socket) => {
  socket.on(types.CHAT, (data: Client) => {
    sessionController(data, socket);
  });
};

server.on(types.OPEN_CONNECTION, eventListener);
