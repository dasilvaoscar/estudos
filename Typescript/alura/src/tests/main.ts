import Negociacao from '../models/Negociacao';

const negociacoes: Array<Negociacao> = []; 

for (let i = 0; i < 10; i++) {
    negociacoes.push(new Negociacao(new Date, i, i))
}

console.log(negociacoes)