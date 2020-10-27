 import {Conta} from '../interfaces/Conta.js'
 
 export class ContaCorrente extends Conta {

    sacar(valor) {
        if(this.getSaldo() < valor) return
        const taxa = valor * 0.1

        this.saldo -= (valor + taxa)
        console.log(`Saldo Atual: R$ ${this.getSaldo()}`)
    }

}