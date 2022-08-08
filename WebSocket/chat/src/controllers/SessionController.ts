import { Client } from '@/interfaces/client';
import { Socket } from 'socket.io';
import { Message } from '@/core/domains/message';
import { SessionUseCase } from '@/core/useCases/session.useCase';
import * as types from '@/utils/types';

const sessionUseCase = new SessionUseCase();

export const sessionController = (data: Client, socket: Socket) => {
  const session = !data.sessionId
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
