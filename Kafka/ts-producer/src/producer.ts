import { KafkaExecuter } from './kafka';

const kafkaExecuter = new KafkaExecuter();

setInterval(() => {
  kafkaExecuter
    .sendMessage('test', { name: 'Oscar' })
    .then(console.log)
    .catch(console.log);
}, 2000);
