export interface Client {
  sessionId?: string;
  fromUserUUID: string;
  toUserUUID: string;
  message: string;
}
