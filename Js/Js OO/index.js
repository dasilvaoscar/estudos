import {Cliente} from './modules/entities/Client.js'
import {ContaCorrente} from './modules/entities/ContaCorrente.js'

const cliente1 = new Cliente("Ricardo", "11122233309");
const cliente2 = new Cliente('Oscar da Silva', "07267865941")

const contaCorrenteRicardo = new ContaCorrente(1001, cliente1);
const contaCorrenteOscar = new ContaCorrente(1002, cliente2)

contaCorrenteRicardo.depositar(-100);
contaCorrenteRicardo.depositar(100);
contaCorrenteRicardo.depositar(100);
contaCorrenteRicardo.sacar(50);

contaCorrenteRicardo.transferir(100, contaCorrenteOscar);


console.log(contaCorrenteOscar);