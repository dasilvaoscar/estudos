function imprimirSoma(a ,b){
    console.log(a + b)
}

imprimirSoma(2, 7)

function Soma(a , b = 0){
    return console.log(a + b)
}

Soma(5)


const func = function Subtracao(a = 0, b = 0){
    return console.log(a - b)
}

func(5, 10)