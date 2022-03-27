import { LoggerPort } from '@/ports/logger.port';
import { createLogger, Logger, format, transports } from 'winston';

export class WinstonLogger implements LoggerPort {
  private logger: Logger;

  constructor(service: string) {
    this.logger = createLogger({
      format: format.combine(format.splat(), format.simple()),
      defaultMeta: { service: service },
      transports: [new transports.Console()],
    });
  }

  log(message: string): void {
    this.logger.log('info', message);
  }
}
