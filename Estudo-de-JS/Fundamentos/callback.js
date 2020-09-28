const somaCallBack = (a, b, callBack) => {
    return callBack(a + b)
}

// 1° e 2° parâmetro(a, b) são as variáveis que serão somadas e o 3° chamará uma função
// que pega o resultado da func pricipal e transforma  
console.log(somaCallBack(20, 2, (total) => {
    return total * 2
} ))