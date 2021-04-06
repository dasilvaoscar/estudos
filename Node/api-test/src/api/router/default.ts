import { Router } from 'express'
import { home } from '../controller/index'

export const router = Router()

router.use('/', home)