import { Controller, Get } from 'npm:@nestjs/common';
import { AppService } from './app.service.ts';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
