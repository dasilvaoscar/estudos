import { Request, Response } from 'express';


const requestsTest = (req: Request, res: Response, next: any) => {
  next()
}

export {
  requestsTest
}