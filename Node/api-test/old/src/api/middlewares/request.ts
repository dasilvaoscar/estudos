import { Request, Response } from 'express';


export const requestsTest = (req: Request, res: Response, next: any) => {
  next()
}
