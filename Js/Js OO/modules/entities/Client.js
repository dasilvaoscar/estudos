export class Cliente{
    
    constructor(nome, cpf){
        this.nome = nome;
        this.cpf = cpf;
    };

    setNome(valor) {
        if(!valor) return;

        this.nome = valor;
    };

    setCpf(valor) {
        if(!valor) return;

        this.cpf = valor;
    };
}

