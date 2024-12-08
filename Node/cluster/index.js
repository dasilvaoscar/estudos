import cluster from 'node:cluster';
import http from 'node:http';
import { availableParallelism } from 'node:os';
import process from 'node:process';

const numCPUs = availableParallelism();

function createInstances() {
  if (cluster.isPrimary) {
    console.log(`Number of CPU Threads: ${numCPUs}`)

    for (let i = 0; i < numCPUs; i++) {
      cluster.fork();
    }

    cluster.on('message', (worker, message) => {
      console.log(`PID: ${worker.process.pid} | Message ${JSON.stringify(message)}`);
    })

    cluster.on('fork', (worker) => {
      console.log(`Worker ${worker.process.pid}`);
    })

    cluster.on('exit', (worker) => {
      console.log(`worker ${worker.process.pid} died`);
    });
  }
}

createInstances()

if (!cluster.isPrimary) {
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end('hello world\n');
    process.send({ cmd: 'notifyRequest' })
  }).listen(8000);
}