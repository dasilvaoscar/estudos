const fetch = require("node-fetch");

const api = fetch('https://api.github.com/OscarSilvaOfficial')

let teste = 'nada ainda'

api.then(res => teste = res)

setTimeout(() => {
  console.log(teste)
}, 1000)