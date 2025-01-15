import { createReadStream } from 'fs';

export async function DownloadController(request) {
  const fileName = 'test.zip'

  try {
    const fileStream = createReadStream(fileName);
    return fileStream
  } catch (error) {
    fastify.log.error(error);
    return {
      status: 500
    }
  }
}