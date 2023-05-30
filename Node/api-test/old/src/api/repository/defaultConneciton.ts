import { createConnection } from "typeorm";
import { User } from './models/User';
import { env } from '../env'


export class Connection {

  static MySqlConnect(): void {
    createConnection({
      type: "mysql",
      host: env.HOST,
      port: env.DB_PORT,
      username: env.USERNAME,
      password: env.PASSWD,
      database: env.DB,
      entities: [
        __dirname + "/models/*.ts"
      ],
      synchronize: true,
      logging: false
    })
    .then(connection => { console.log(`DB Is connect: ${connection.isConnected}`)})
    .catch(error => console.log(error));
  }

}