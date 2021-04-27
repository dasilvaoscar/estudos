class NegociacaoView {

  constructor(protected _data?: Date, protected _quantidade?: number, protected _valor?: number) {}

  get data(): Date{
    if(!this._data) {
      throw("Construtor não inicializado");
    }
    return this._data
  }

  get quantidade(): number {
    if(!this._quantidade) {
      throw("Construtor não inicializado");
    }
    return this._quantidade;
  }

  get valor(): number {
    if(!this._valor) {
      throw("Construtor não inicializado");
    }
    return this._valor;
  }
  
}

export default NegociacaoView