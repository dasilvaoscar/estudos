export interface IMessage {
  userUUID: string;
  message: string;
}

export class Message implements IMessage {
  private __userUUID: string;
  private __message: string;

  constructor(data: IMessage) {
    this.__userUUID = data.userUUID;
    this.__message = data.message;
  }

  get userUUID(): string {
    return this.__userUUID;
  }

  get message(): string {
    return this.__message;
  }
}
