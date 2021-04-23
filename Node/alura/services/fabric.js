import express from 'express'
import Routes from '../routes/urls.js'

class Fabric {

  constructor() {
    this.app = express()
  }

  buildApp() {
    this.app.use(
      express.json(), Routes
    )
    return this.app
  }

}

export default Fabric