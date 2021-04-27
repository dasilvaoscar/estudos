import env from 'dotenv'

env.config()

export const vars = {
  PORT: process.env.PORT
}