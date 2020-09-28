const mongo = require('mongoose');
const Schema = mongo.Schema;

let SmartPhoneSchema = new Schema({
    nome: {
        type: String,
        required: true,
        max: 100
     },
    marca: {
        type: Number, 
        required: true
    }
});

module.exports = mongo.model('Smartphone', SmartPhoneSchema);