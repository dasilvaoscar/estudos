import { Buffer } from 'node:buffer'

export class FastJSON {
  static jsonToBinary(data) {
    return Buffer.from(JSON.stringify(data))
  }

  static binaryToJson(buffer) {
    return JSON.parse(buffer.toString())
  }
}
