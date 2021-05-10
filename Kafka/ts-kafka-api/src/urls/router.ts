import { Router } from 'express'
import { producer } from '../services/kafka'

const url = Router()

url.get('/', producer)

export default url