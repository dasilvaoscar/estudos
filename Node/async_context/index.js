const { AsyncLocalStorage } = require("node:async_hooks");
const http = require('http')

const asyncLocalStorage = new AsyncLocalStorage();

let id = 1

function logWithId(msg) {
  const currentId = asyncLocalStorage.getStore();
  console.log(`${currentId}:`, msg);
  id++
}

http
  .createServer((_req, res) => {
    asyncLocalStorage.run(id, () => {
      setImmediate(() => {
        logWithId("finish");
        res.end();
      });
    });
  })
  .listen(8080);
