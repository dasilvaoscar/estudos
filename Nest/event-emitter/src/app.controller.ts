import { EventEmitter2 as EventEmitter } from '@nestjs/event-emitter';
import { Controller, Post } from '@nestjs/common';

@Controller('/event')
export class AppController {
  constructor(private eventEmitter: EventEmitter) {}

  @Post('/')
  test() {
    return this.eventEmitter.emit('order.created', {
      message: 'A simple Test',
    });
  }
}
