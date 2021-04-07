"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Connection = void 0;
const typeorm_1 = require("typeorm");
const env_1 = require("../env");
class Connection {
    static MySqlConnect() {
        typeorm_1.createConnection({
            type: "mysql",
            host: env_1.env.HOST,
            port: env_1.env.DB_PORT,
            username: env_1.env.USERNAME,
            password: env_1.env.PASSWD,
            database: env_1.env.DB,
            entities: [
                __dirname + "/models/*.ts"
            ],
            synchronize: true,
            logging: false
        })
            .then(connection => { console.log(`DB Is connect: ${connection.isConnected}`); })
            .catch(error => console.log(error));
    }
}
exports.Connection = Connection;
//# sourceMappingURL=defaultConneciton.js.map