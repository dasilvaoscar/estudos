export class Cliente{
    #nome;
    #cpf;

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

