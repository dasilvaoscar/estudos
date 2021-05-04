import { Pessoa, RecebeStringERetornaString, RelogioInterface } from './interfaces'

function criarPessoa(pessoa: Pessoa): Pessoa {
  return pessoa
}

const oscar: Pessoa = criarPessoa({
  nome: 'Oscar',
  idade: 20,
  cpf: 7267865941
})

const myFuncTest: RecebeStringERetornaString = (fname, lname) => {
  return `${fname} ${lname}`
}

console.log(oscar.nome = 'da Silva')
console.log(myFuncTest("Teste", "da Silva"))

class Relogio implements RelogioInterface {
  hora: Date = new Date();
}

const hora = new Relogio()

console.log(hora.hora)