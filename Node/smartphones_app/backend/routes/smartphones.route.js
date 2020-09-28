const express = require('express');
const router = express.Router();

const controller = require('../controllers/smartphones.controller');

router.get('/testar', controller.test)

module.exports = router;