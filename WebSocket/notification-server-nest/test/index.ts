import { Manager } from 'socket.io-client';

const SOCKET_URL = 'ws://localhost:3000';
const EVENT_NAMESPACE = '/event';

const manager = new Manager(SOCKET_URL);
const socket = manager.socket(EVENT_NAMESPACE);

const EVENT_CHANNEL = 'newMessage';
socket.emit(EVENT_CHANNEL, {
  timeSent: new Date(Date.now()).toLocaleString('pt-BR'),
  message: 'Meu teste',
});

const RESPONSE_CHANNEL = 'DEFAULT_RESPONSE_CHANNEL';
socket.on(RESPONSE_CHANNEL, (e) => {
  console.log(e);
});
