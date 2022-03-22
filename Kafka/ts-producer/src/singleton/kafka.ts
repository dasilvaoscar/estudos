import { Kafka } from 'kafkajs';

export class KafkaSingleton {
  private static instance: Kafka;

  private constructor() {
    KafkaSingleton.instance = new Kafka({
      clientId: 'my-app',
      brokers: ['localhost:9092'],
      retry: {
        initialRetryTime: 300,
        retries: 10,
      },
    });
  }

  public static getInstance(): Kafka {
    if (!KafkaSingleton.instance) new KafkaSingleton();
    return KafkaSingleton.instance;
  }
}
