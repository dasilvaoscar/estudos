"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.UserController = void 0;
const User_1 = require("../repository/models/User");
class UserController {
    static home(req, res) {
        return __awaiter(this, void 0, void 0, function* () {
            const response = yield User_1.User.find();
            res.send(response);
        });
    }
    static createUser(req, res) {
        return __awaiter(this, void 0, void 0, function* () {
            console.log(req.body);
            UserController.user.firstName = 'Oscar';
            UserController.user.lastName = 'da Silva';
            UserController.user.age = 20;
            try {
                yield UserController.user.save();
            }
            catch (e) {
                res.send(e);
            }
            res.send('ok');
        });
    }
}
exports.UserController = UserController;
UserController.user = new User_1.User();
/* export async function home(req: Request, res: Response) {
  const user = new User()

  const response = await User.find()
  res.send(response)
} */
/* export async function createUser(req: Request, res: Response) {
  const user = new User()

  user.firstName = 'Oscar'
  user.lastName = 'da Silva'
  user.age = 20
  await user.save()
} */ 
//# sourceMappingURL=index.js.map