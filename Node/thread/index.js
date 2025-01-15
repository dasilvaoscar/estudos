import { isMainThread, Worker, workerData, parentPort } from 'node:worker_threads'

import { havyOperation } from './test.js'


// Executa 2x | Demora 10 segundos
async function testWithoutThreads(numberOfExecutions=2) {
  console.time('no-worker')

  const executions = Array.from({ length: numberOfExecutions })

  let index = 0
  for (const _ of executions) {
    await havyOperation()
    console.log(`${index} execution`)
    index++
  }

  console.timeEnd('no-worker')
}

// Executa 100 | Demora 5 segundos
async function testWithThreads(numberOfExecutions=100) {
  console.time('worker')
  
  if (isMainThread) {
    const executions = Array.from({ length: numberOfExecutions })
    const workers = executions.map(() => new Worker('./index.js'))
    const messageListener = (worker, index) => worker.on('message', (result) => console.log(`${index + 1} Thread`, result))
    workers.forEach(messageListener)
  } else {
    const result = await havyOperation()
    parentPort.postMessage(result);
  }

  console.timeEnd('worker')
}

testWithThreads()
