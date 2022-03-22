import { KafkaExecuter } from '../kafka';

const kafkaBroker = new KafkaExecuter();

export const CreateListTopics = async () => {
  const topics = [{ topic: 'test' }];
  await kafkaBroker.createTopic(topics);
  console.log(await kafkaBroker.listTopics());
};
