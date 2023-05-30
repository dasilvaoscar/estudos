import { Router } from 'express'
import { UserController } from '../controller/index'

export const router = Router()

router.get('/', UserController.selectUser)
router.post('/', UserController.createUser)
router.delete('/:user_id', UserController.deleteUser)