import express from "express";
import { Server } from "typescript-rest";
import Controllers from "./controllers/index"

new Controllers

let app: express.Application = express();
Server.buildServices(app);

app.listen(3000, function() {
  console.log('Rest Server listening on port 3000!');
});