import { Message } from './message';

export interface ISession {
  id: string;
  usersUUID: string[];
  messages: Message[];
  addMessage: (message: Message) => void;
}

export class Session implements ISession {
  private __id: string;
  private __usersUUID: string[];
  private __messages: Message[];

  constructor(data: { id: string; usersUUID: string[] }) {
    this.__id = data.id;
    this.__usersUUID = data.usersUUID;
  }

  get id(): string {
    return this.__id;
  }

  get usersUUID(): string[] {
    return this.__usersUUID;
  }

  get messages(): Message[] {
    return this.__messages;
  }

  addMessage(message: Message): void {
    this.__messages.push(message);
  }
}
