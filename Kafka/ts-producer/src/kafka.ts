import { randomUUID } from 'crypto';
import { ITopicConfig, Kafka } from 'kafkajs';
import { KafkaSingleton } from './singleton/kafka';

export class KafkaBroker {
  kafkaInstance: Kafka;

  constructor() {
    this.kafkaInstance = KafkaSingleton.getInstance();
  }

  async listTopics(): Promise<any> {
    const admin = this.kafkaInstance.admin();
    await admin.connect();
    return await admin.listTopics();
  }

  async createTopic(topics: ITopicConfig[]): Promise<any> {
    const admin = this.kafkaInstance.admin();
    await admin.connect();
    await admin.createTopics({
      validateOnly: false,
      waitForLeaders: false,
      timeout: 1000,
      topics: topics,
    });
  }

  async sendMessage(topic: string, message: object): Promise<any> {
    const producer = this.kafkaInstance.producer();
    await producer.connect();
    return await producer.send({
      topic: topic,
      messages: [{ value: JSON.stringify(message), key: randomUUID() }],
    });
  }

  async consumer(topic: string, group: string): Promise<any> {
    const consumer = this.kafkaInstance.consumer({ groupId: group });
    await consumer.connect();
    await consumer.subscribe({ topic: topic });
    await consumer.run({
      eachMessage: async ({ topic, partition, message }) => {
        const prefix = `${topic}[${partition} | ${message.offset}] / ${message.timestamp}`;
        const messageDesc = `Key: ${message.key} | Value: ${message.value}`;
        console.log(`------------------------------------`);
        console.log(`- Prefix: ${prefix} | ${messageDesc}`);
      },
    });
  }
}
