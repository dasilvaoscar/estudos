export class Cliente{
    #nome;
    #cpf;

    setNome(valor) {
        if(!valor) return

        this.nome = valor
    }

    setCpf(valor) {
        if(!valor) return

        this.cpf = valor
    }
}

