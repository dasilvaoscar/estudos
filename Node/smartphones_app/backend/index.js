const express = require('express');
const bodyParser = require('body-parser');

//Access DB
const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://teste:<password>@cluster0.xlh9q.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true }); 

client.connect(err => {
    const collection = client.db("test").collection("devices");
    // perform actions on the collection object
    client.close();
});

//Routs
const app = express();
const smartphone = require('./routes/smartphones.route');
app.use('/smartphones', smartphone);

//Body Parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use('/', smartphone);

//Server
app.listen(8000, () => {
    console.log('Servidor em execução na porta ' + 8000)
});