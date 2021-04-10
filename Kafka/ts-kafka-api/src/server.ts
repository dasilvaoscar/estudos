import express from "express" 

const app = express()
const port = 5000

app.use(
  express.json(), express.urlencoded({extended: false })
)

app.listen(port, () => {
  console.log(`Run at port ${port}`)
})