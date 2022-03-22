import { KafkaExecuter } from './kafka';

const kafkaExecuter = new KafkaExecuter();

kafkaExecuter
  .consumer('test', 'primeiro-grupo')
  .then(console.log)
  .catch(console.log);
