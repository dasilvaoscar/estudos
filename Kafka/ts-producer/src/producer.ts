import { KafkaBroker } from './kafka';

const kafkaBroker = new KafkaBroker();

setInterval(() => {
  kafkaBroker
    .sendMessage('test', { name: 'Oscar' })
    .then(console.log)
    .catch(console.log);
}, 2000);
