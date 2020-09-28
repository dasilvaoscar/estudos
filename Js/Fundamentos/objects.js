const pessoa = {
    nome: 'Oscar',
    sobrenome: 'da Silva',
    idade: 19,
    altura: 1.70,
    docs: {
        cpf: '072.678.659-41',
        rg: '7272312',
        empresas: {
            cnpj: ['122.413.690.001-75', '1234567891011']
        }
    }
}

// Add atributo função no objeto pessoa
pessoa.func = (nome) => {
    console.log(nome)
}

pessoa.func(pessoa)

let novoObjeto = {
    nome: 'Oscar',
    idade: 19,
    pais: 'Brasil'
}

const { nome: nomeDaVar } = novoObjeto
pessoa.func(nomeDaVar)