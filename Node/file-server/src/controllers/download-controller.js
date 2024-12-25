import { createReadStream } from 'fs';

export async function DownloadController(request, reply) {
  const fileName = 'test.zip'

  try {
    const fileStream = createReadStream(fileName);
    return fileStream
  } catch (error) {
    fastify.log.error(error);
    reply.status(500).send('Internal Server Error');
  }
}