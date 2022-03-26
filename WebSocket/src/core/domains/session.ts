import { IMessage } from './message';

export interface ISession {
  id?: string;
  usersUUID: string[];
  messages: IMessage[];
  addMessage(message: IMessage): void;
}

export class Session implements ISession {
  private __id: string;
  private __usersUUID: string[];
  private __messages: IMessage[];

  constructor(data: ISession) {
    this.__id = data.id;
    this.__usersUUID = data.usersUUID;
    this.__messages = data.messages;
  }

  get id(): string {
    return this.__id;
  }

  get usersUUID(): string[] {
    return this.__usersUUID;
  }

  get messages(): IMessage[] {
    return this.__messages;
  }

  addMessage(message: IMessage): void {
    this.__messages.push(message);
  }
}
