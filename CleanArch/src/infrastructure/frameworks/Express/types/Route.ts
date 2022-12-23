import { Request, Response } from "express";


export type Route = {
  method: string;
  path: string;
  callback: (req: Request, res: Response) => void;
};
