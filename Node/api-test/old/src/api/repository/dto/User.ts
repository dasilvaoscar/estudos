import { User } from '../models/User'


export class DTOUser {
  
  static user = new User

  getUser(kwargs: any) {

    DTOUser.user.firstName = kwargs.first_name ? kwargs.firstName:kwargs.first_name
    DTOUser.user.lastName = kwargs.last_name ? kwargs.lastName:kwargs.last_name
    DTOUser.user.age = kwargs.age

    return DTOUser.user
    
  }


}