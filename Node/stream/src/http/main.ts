import { createServer, IncomingMessage, ServerResponse } from 'http';

const callback = (req: IncomingMessage, res: ServerResponse) => {
  const chunkDetails = (chunk: Buffer) => {
    try {
      console.log(JSON.parse(JSON.stringify(chunk.toString())));
    } catch {
      console.log(chunk.toString());
    }
  };

  req.on('data', chunkDetails);

  res.end('Hello World');
};

const server = createServer(callback);
server.listen(3000);
