import {Cliente} from './modules/entities/Client.js'
import {ContaCorrente} from './modules/entities/ContaCorrente.js'

const cliente1 = new Cliente("Ricardo", "11122233309");
const cliente2 = new Cliente('Oscar da Silva', "07267865941")

const contaCorrenteRicardo = new ContaCorrente(1001, cliente1);
const contaCorrenteOscar = new ContaCorrente(1002, cliente2)

contaCorrenteOscar.depositar(1000)
contaCorrenteOscar.sacar(100)