import { Request, Response } from "express";
import { Route } from "../frameworks/Express/types/Route";
import { HttpMethods } from "../utils/enums/HttpMethods";

export const routes: Route[] = [
  {
    method: HttpMethods.GET,
    path: "/",
    callback: (_req: Request, res: Response) => {
      res.send("Bla");
    },
  },
  {
    method: HttpMethods.POST,
    path: "/",
    callback: (req: Request, res: Response) => {
      res.json(req.body);
    },
  },
];