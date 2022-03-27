import { Server } from 'socket.io';
import { Session } from '@/core/domains/session';
import { randomUUID } from 'crypto';
import { Message } from './core/domains/message';
import * as types from '@/utils/types';

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

const createSession = (fromUserUUID: string, toUserUUID: string): Session => {
  return new Session({
    id: randomUUID(),
    usersUUID: [fromUserUUID, toUserUUID],
  });
};

const getSession = (sessionId: string): Session => {
  return new Session({
    id: sessionId,
    usersUUID: [],
  });
};

const createMessage = (message: string, userUUID: string) => {
  return new Message({
    message: message,
    userUUID: userUUID,
  });
};

const sessionController = (data: Client) => {
  const session: Session = !data.sessionId
    ? createSession(data.fromUserUUID, data.toUserUUID)
    : getSession(data.sessionId);

  const message = createMessage(data.message, data.fromUserUUID);

  session.addMessage(message);
};

const eventListener = (socket) => socket.on(types.CHAT, sessionController);

server.on(types.OPEN_CONNECTION, eventListener);
