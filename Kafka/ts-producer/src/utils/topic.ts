import { KafkaBroker } from '../kafka';

const kafkaBroker = new KafkaBroker();

export const CreateListTopics = async () => {
  const topics = [{ topic: 'test' }];
  await kafkaBroker.createTopic(topics);
  console.log(await kafkaBroker.listTopics());
};
