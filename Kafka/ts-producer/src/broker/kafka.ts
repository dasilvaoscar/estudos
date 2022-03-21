import { ITopicConfig } from 'kafkajs';
import { KafkaSingleton } from '../singleton/kafka';

export class KafkaBroker {
  kafkaInstance: any;
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
      waitForLeaders: true,
      timeout: 1000000,
      topics: topics,
    });
  }

  async sendMessage(topic: string, message: object): Promise<any> {
    const producer = this.kafkaInstance.producer();
    await producer.connect();
    return await producer.send({
      topic: topic,
      messages: [{ value: JSON.stringify(message) }],
    });
  }
}
