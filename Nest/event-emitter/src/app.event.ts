import { Injectable } from '@nestjs/common';
import { OnEvent } from '@nestjs/event-emitter';

@Injectable()
export class Events {
  @OnEvent('order.created')
  handleEverything(payload: any) {
    setTimeout(() => {
      console.log(payload);
    }, 4000);
  }
}
