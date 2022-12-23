import express, { Express } from "express";
import { WebServer } from '../../../contracts/WebServer'
import { Route } from "./types/Route";

export class ExpressServer implements WebServer {
  constructor(private readonly routes: Route[], private readonly server: Express) {}
  
  run(): void {
    this.createRoutes();
    this.server.listen(8000, () => console.log("Server running"));
  }

  private createRoutes() {
    this.routes.map((route) => {
      const router = this.server as any;
      router[route.method](route.path, route.callback);
    });
  }
  
  static create(routes: Route[]): WebServer {
    return new ExpressServer(routes, express());
  }
}

