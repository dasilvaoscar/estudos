import Fabric from './services/fabric.js'

const app = new Fabric().buildApp()

app.listen(3000, () => {
  console.log("Run at port 3000")
})