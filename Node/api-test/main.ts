import express from 'express'
import "reflect-metadata";
import { env } from './env'
import { router } from './src/api/router/default'
import { requestsTest } from './src/api/middlewares/request'
import { Connection } from './src/api/repository/defaultConneciton'

const app = express()

Connection.MySqlConnect()

app.use(router, requestsTest)

app.listen(env.PORT, () => {
  console.log(`Server on | PORT ${env.PORT}`)
})