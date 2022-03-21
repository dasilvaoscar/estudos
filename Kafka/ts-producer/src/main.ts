import { KafkaBroker } from './broker/kafka';

const kafkaBroker = new KafkaBroker();

const CreateListTopics = async () => {
  const topics = [{ topic: 'test' }];
  await kafkaBroker.createTopic(topics);
  console.log(await kafkaBroker.listTopics());
};

kafkaBroker
  .sendMessage('test', { name: 'Oscar' })
  .then(console.log)
  .catch(console.log);
