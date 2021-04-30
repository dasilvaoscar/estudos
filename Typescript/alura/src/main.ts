import express from "express";
import { Application } from "express"
import { Server } from "typescript-rest";
import Controllers from "./controllers/index"

new Controllers

const app: Application = express();
Server.buildServices(app);

app.listen(3000, function() {
  console.log('Rest Server listening on port 3000!');
});