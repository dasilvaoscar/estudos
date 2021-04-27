import { index } from '../controller/index'
import { Router } from 'express'

export const router = Router()

router.get('/', index)