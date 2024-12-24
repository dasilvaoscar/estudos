import { FastJSON } from './modules/core.js'

const binaryJson = FastJSON.jsonToBinary({ name: 'Oscar' })
const json = FastJSON.binaryToJson(binaryJson)

console.log(`Dado binário`, binaryJson)
console.log(`Dado convertido`, json)