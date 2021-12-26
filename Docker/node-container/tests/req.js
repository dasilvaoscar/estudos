const https = require('axios');
const { Worker, workerData } = require('worker_threads')

const runTest = () => {
  const url = 'http://localhost'
  for(let i = 0; i < 1000; i++) {
    https.get(url)
  }
}

setInterval(runTest, 1000)