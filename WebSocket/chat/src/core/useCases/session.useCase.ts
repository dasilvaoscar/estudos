import { Session } from '../../core/domains/session';
import { randomUUID } from 'crypto';

export interface ICreateSession {
  fromUserUUID: string;
  toUserUUID: string;
}

export class SessionUseCase {
  getSession(sessionId: string): Session {
    return new Session({
      id: sessionId,
      usersUUID: [],
    });
  }

  createSession(info: ICreateSession): Session {
    return new Session({
      id: randomUUID(),
      usersUUID: [info.fromUserUUID, info.toUserUUID],
    });
  }
}
