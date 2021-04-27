import NegoficacaoView from '../views/NegoficacaoView'

class Negociacao extends NegoficacaoView {

  get volume(): number {
    if(!this._quantidade || !this._valor) {
      throw("Construtor não definido")
    }
    return this._quantidade * this._valor;
  }

}

export default Negociacao