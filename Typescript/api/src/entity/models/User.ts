import { Iuser } from '../interfaces/Iuser'

export class User {
  private _id: number;
  private _userName: string;
  private _firstName: string;
  private _lastName: string;

  constructor({userName, firstName, lastName}: Iuser) {
    this._id = 0;
    this._userName = userName
    this._firstName = firstName
    this._lastName = lastName
  }

  get id(): number {
    return this._id
  }
  
  get userName(): string {
    return this._userName
  }

  get firstName(): string {
    return this._firstName
  }

  get lastName(): string {
    return this._lastName
  }

  set userName(uName: string) {
    this._userName = uName  
  }

  set firstName(fName: string) {
    this._firstName = fName 
  }

  set lastName(lName: string) {
    this._lastName = lName
  }

}