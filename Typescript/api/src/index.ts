import { vars as env } from './configs/enviroment'
import express from 'express'
import { index } from './controller/index'

const app = express()
const port = env.PORT

app.use(index)


app.listen(port, () => {
  console.log(`Running on: http://localhost:${port} ⌨ 🚀 🖥️`)
})