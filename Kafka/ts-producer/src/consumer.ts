import { KafkaBroker } from './broker/kafka';

const kafkaBroker = new KafkaBroker();

kafkaBroker
  .consumer('test', 'primeiro-grupo')
  .then(console.log)
  .catch(console.log);
