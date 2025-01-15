import { DownloadController } from './controllers/download-controller.js'

const handler = async (event) => {
  try {
    await DownloadController(event, reply)
    return {
      statusCode: 200,
      body: JSON.stringify('Ok')
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify('Error message', err.message)
    };
  }
};

export { handler }