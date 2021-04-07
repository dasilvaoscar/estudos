"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.env = void 0;
const ts_dotenv_1 = require("ts-dotenv");
exports.env = ts_dotenv_1.load({
    PORT: Number,
    HOST: String,
    DB_PORT: Number,
    USERNAME: String,
    PASSWD: String,
    DB: String
});
//# sourceMappingURL=env.js.map