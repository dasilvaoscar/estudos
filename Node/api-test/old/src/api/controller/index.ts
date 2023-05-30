import { Request, Response } from 'express';
import { User } from '../repository/models/User'
import { DTOUser } from '../repository/dto/User'


export class UserController {
  
  static dtoUser = new DTOUser()
  static erro500: object = {"erro": '500'}

  static async selectUser(req: Request, res: Response) {

    const response = await User.find()
    res.json(response)         

  }

  static async createUser(req: Request, res: Response) {
  
    const user = UserController.dtoUser.getUser(req.body)
    
    try {
      user.save()
    } catch(e) {
      res.json(this.erro500)
    }

    const response = !user.id ? 
      'Usuário inserido': {"user_id": user.id}

    res.json(response)

  }

  static async deleteUser(req: Request, res: Response) {
    
    const user_id: number = parseInt(req.params.user_id)
    
    try {

      const userExists = await User.findOne(user_id)
      
      if (!userExists) {
        res.json('Usuário não existe')
      } else {
        User.delete(user_id)
      }

    } catch(e) {
      res.json(this.erro500)
    }

    res.json('Usuário deletado')
  }
}
