import { Request, Response } from 'express';
import { User } from '../repository/models/User'

export async function home(req: Request, res: Response) {
  res.send('ok')
}