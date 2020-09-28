console.log('/* ************  Variáveis ************** */')

// Data Types
// A palavra reservada let sinaliza uma variável
// A palavra reservada const sinaliza uma constante

let string = 'Var do tipo String'
const int = 5
let float = 3.6

console.log('String: ' + string)
console.log('Integer: ' + int)
console.log('Float: ' + float)

console.log('/* ************  Conversão ************** */')

// toFixed defina a quantidade de casas decimais
float = float.toFixed(5)

console.log('A Variável Float foi convertida em: ' + typeof float + ' = ' + float)