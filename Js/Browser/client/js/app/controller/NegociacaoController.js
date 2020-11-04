class NegociacaoController {

    constructor() {
        this._data = document.getElementById('data'),
        this._quantidade = document.getElementById('quantidade'),
        this._valor = document.getElementById('valor')
    };
    

    adiciona(event) {
        event.preventDefault();

        const model = new Negociacao(
            new Date(this._data.value.split('-')),
            this._quantidade.value,
            this._valor.value
        )      
        
        console.log(model.data)
    }    
}




