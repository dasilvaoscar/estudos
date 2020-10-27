import {Cliente} from './Client.js'
import {ContaCorrente} from './ContaCorrente.js'

const cliente1 = new Cliente();
cliente1.setNome("Ricardo");
cliente1.setCpf(11122233309);

const cliente2 = new Cliente()
cliente2.setNome('Oscar da Silva')
cliente2.setCpf('07267865941')


const contaCorrenteRicardo = new ContaCorrente();
contaCorrenteRicardo.setAgencia(1001);

const contaCorrenteOscar = new ContaCorrente()
contaCorrenteOscar.setAgencia(1002)

contaCorrenteRicardo.depositar(-100);
contaCorrenteRicardo.depositar(100);
contaCorrenteRicardo.depositar(100);
contaCorrenteRicardo.sacar(50);
contaCorrenteRicardo.setCliente(cliente1)
contaCorrenteOscar.setCliente(cliente2)

contaCorrenteRicardo.transferir(100, contaCorrenteOscar)


console.log(contaCorrenteOscar)