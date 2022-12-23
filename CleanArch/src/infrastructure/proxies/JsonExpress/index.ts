import { WebServer } from "../../../contracts/WebServer";
import { Route } from "../../frameworks/Express/types/Route";
import { ExpressServer } from '../../frameworks/Express'
import express from "express";

export class JsonExpress implements WebServer {
  constructor(private readonly webserver: WebServer) {}

  run(): void {
    this.webserver.run()
  }

  static create(routes: Route[]): WebServer {
    const app = express()
    app.use(express.json())
    const webserver = new ExpressServer(routes, app)
    return new JsonExpress(webserver)
  }
}