import { Module } from '@nestjs/common';
import { EventGateway } from './event.gateway';

@Module({
  // imports: [EventGateway],
  // controllers: [],
  providers: [EventGateway],
})
export class AppModule {}
