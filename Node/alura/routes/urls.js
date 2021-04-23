import express from 'express'
import Controller from '../services/main.js'

const router = express.Router()
const controller = new  Controller()

router.get('/', controller.index)

export default router