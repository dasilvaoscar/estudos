import { Request, Response } from 'express'
import {IProducerConfig, ProducerConfig, SimpleProducer} from "kafka-typescript"
import rdkafka from "node-rdkafka"

class kafka {

  rdkafkaProducer: any
  producerConfig: any

  constructor() {
    this.rdkafkaProducer = rdkafka.Producer
    this.producerConfig = 
  }
}

const configs = {
  rdkafkaProducer: rdkafka.Producer,
  producerConfig: new ProducerConfig("localhost", "9092") 
}
const producers: { [topic: string]: SimpleProducer } = {}

async function createTopicProducer(topic: string, config: IProducerConfig) {
  const prod = await new SimpleProducer()
    .create(configs.rdkafkaProducer, config)    
    .connect()

  prod.setTopic(topic);
  producers[topic] = prod
  return prod
}

async function producer(req: Request, res: Response) {
  await createTopicProducer("hello-world", configs.producerConfig)
    .then(x => {
      producers["hello-world"].send("1", Buffer.from("hello"));
    })
    .catch(err => console.error(err))
  res.send('ok')
}

export {
  producer
}