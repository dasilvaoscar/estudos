import { server } from './shared/index.js' 
import { DownloadController } from './controllers/download-controller.js'


server.get('/download', async (request, reply) => await DownloadController(request, reply));

async function start() {
  try {
    await server.listen({ port: 3000, host: '0.0.0.0' });
  } catch (err) {
    server.log.error(err);
    process.exit(1);
  }
}

start();
