class Test {

    constructor(n1 = 0, n2 = 0){
        this.n1 = n1
        this.n2 = n2
    }

    soma(){
        var soma = this.n1 + this.n2
        return soma
    }

    //Terminar
    tabuada(){
        for(var i = 0; i = 9; i++){
            var re = this.n1 * i
            return console.log(re)
        }
    }
    
}

const t1 = new Test(9)

//console.log(t1.soma())
console.log(t1.tabuada())