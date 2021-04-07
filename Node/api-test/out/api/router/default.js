"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.router = void 0;
const express_1 = require("express");
const index_1 = require("../controller/index");
exports.router = express_1.Router();
exports.router.get('/', index_1.UserController.home);
exports.router.post('/', index_1.UserController.createUser);
//# sourceMappingURL=default.js.map