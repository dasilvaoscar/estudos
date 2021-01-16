import { Request, Response } from 'express'
import { User } from '../entity/models/User'
import { getDate } from '../utils/utils'
const debug = require('debug')('api:index')

const index = (req: Request , res: Response) => {
  debug(req.query, `access at: ${getDate()}`)

  const user = new User({
    userName: 'oscar.silva',
    firstName: 'Oscar',
    lastName: 'da Silva'
  });
  
  return res.json(user)
}

export { index }