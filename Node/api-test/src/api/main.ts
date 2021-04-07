import "reflect-metadata"
import express from 'express'
import { env } from './env'
import { router } from './router/default'
import { requestsTest } from './middlewares/request'
import { Connection } from './repository/defaultConneciton'

const app = express()
Connection.MySqlConnect()

app.use(
  express.json(),
  express.urlencoded({extended: true}),
  router, requestsTest
)

app.listen(env.PORT, () => {
  console.log(`Server on | PORT ${env.PORT}`)
})