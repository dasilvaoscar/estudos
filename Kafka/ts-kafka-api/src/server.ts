import express from "express" 
import urls from './urls/router'

const app = express()
const port = 8080

app.use(
  express.json(), express.urlencoded({extended: false }),
  urls
)

app.listen(port, () => {
  console.log(`Run at port ${port}`)
})