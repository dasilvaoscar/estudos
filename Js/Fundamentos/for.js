const numeros = [1, 2, 4, 5, 3]
let result = 0

function forAntigo(){
    for (let i = 0; i != numeros.length; i++) {
        result = result + numeros[i]
    } return result
}

function forNovo() {
    result = 0
    for (let num of numeros){
        result = result + num
    } return result
}

console.log(`For Antigo: ${forAntigo()}`)
console.log(`For novo: ${forNovo()}`)