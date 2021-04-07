"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
require("reflect-metadata");
const express_1 = __importDefault(require("express"));
const body_parser_1 = __importDefault(require("body-parser"));
const env_1 = require("./env");
const default_1 = require("./router/default");
const request_1 = require("./middlewares/request");
const defaultConneciton_1 = require("./repository/defaultConneciton");
const app = express_1.default();
defaultConneciton_1.Connection.MySqlConnect();
app.use(default_1.router, request_1.requestsTest, body_parser_1.default.json());
app.listen(env_1.env.PORT, () => {
    console.log(`Server on | PORT ${env_1.env.PORT}`);
});
//# sourceMappingURL=main.js.map