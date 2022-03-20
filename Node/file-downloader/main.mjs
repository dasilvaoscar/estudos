import { createServer } from 'http'
import { readFile, createReadStream } from 'fs'
import { promisify } from 'util'

const readFilePromisse = promisify(readFile)

// Isso não vai funcionar pois o arquivo é muito grande
const normal = async (res) => {
  try {
    const response = await readFilePromisse('./file/ubuntu.iso')
    res.send(response)
  } catch (e) {
    console.log(e)
  }
}

const stream = (req, res) => {
  console.log('Stream iniciado...')
  const stream = createReadStream('./file/ubuntu.iso')
  stream.pipe(res)
}

const server = createServer((req, res) => stream(req, res))

server.listen(3000, () => console.log('listening on 3000'))