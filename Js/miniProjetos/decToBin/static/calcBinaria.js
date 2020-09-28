let resto = []

const calcBinToDec = (number) => {
    while(number != 1){
        resto.push(number % 2);
        number = Math.trunc(number / 2);
        if (number == 1){
            break
        }        
    }
    resto.reverse()
    result = String(resto).replace(/,/g,'')
    return `Em BINÁRIO: 1${result}`
}

// Teste da Função
console.log(calcBinToDec(100))