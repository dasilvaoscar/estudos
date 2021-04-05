import { load } from 'ts-dotenv';

export const env = load({
  PORT: Number,
  HOST: String,
  DB_PORT: Number,
  USERNAME: String,
  PASSWD: String,
  DB: String
});