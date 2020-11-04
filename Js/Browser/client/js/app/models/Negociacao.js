class Negociacao {

    constructor(data, valor, quantidade) {
        this._data = new Date(data.getTime()),
        this._valor = valor,
        this._quantidade = quantidade,
        this.db = []
        Object.freeze(this)
    }

    get data() {
        return this._data
    }

    setData(value) {
        this._data = value
    }

    get valor() {
        return this._valor
    }

    setValoe(value) {
        this._valor = value
    }

    get quantidade() {
        return this._quantidade
    }

    setQuantidade(value) {
        this._quantidade = value
    }

    get calculaVolume() {
        return this._quantidade * this._valor
    }

    setNegociacao() {
        this.db.push(data, valor, quantidade, this.calculaVolume())
    }

    get negociacao() {
        return this.db
    }

}