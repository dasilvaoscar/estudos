interface Pessoa {
  nome?: string,
  idade?: number,
  readonly cpf?: number;
}

interface RecebeStringERetornaString {
  (fname: string, lname: string): string
}

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