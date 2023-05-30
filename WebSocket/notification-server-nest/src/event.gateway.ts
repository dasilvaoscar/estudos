/* eslint-disable @typescript-eslint/no-unused-vars */
import {
  MessageBody,
  OnGatewayConnection,
  OnGatewayDisconnect,
  OnGatewayInit,
  SubscribeMessage,
  WebSocketGateway,
  WebSocketServer,
} from '@nestjs/websockets';
import { Logger } from '@nestjs/common';

import { Server, Socket } from 'socket.io';

const RESPONSE_CHANNEL = 'DEFAULT_RESPONSE_CHANNEL';

@WebSocketGateway({ namespace: 'event' })
export class EventGateway
  implements OnGatewayInit, OnGatewayConnection, OnGatewayDisconnect
{
  private logger: Logger = new Logger('AppGateway');

  @WebSocketServer()
  server: Server;

  afterInit(_server: Server) {
    this.logger.log('Initialized .....');
  }

  handleConnection(client: Socket, ...args: any[]) {
    this.logger.log(`Client connected: ${client.id}`);
  }

  handleDisconnect(client: Socket) {
    this.logger.log(`Client disconnected: ${client.id}`);
  }

  @SubscribeMessage('newMessage')
  onNewMessage(@MessageBody() body: any) {
    console.log(body);
    this.server.emit(RESPONSE_CHANNEL, {
      msg: 'New Message',
      content: body,
    });
  }
}
