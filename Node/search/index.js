// executa filter de nomes e mede tempo de execução

const array = ["João", "Maria", "Pedro", "Ana", "Bruno"];

let start = performance.now();
let result = array.filter(item => item.length > 5);
let end = performance.now();

console.log("Resultado do filter: ", result);
console.log(`Tempo de execução: ${end - start}ms`);

// executa busca binaria de nomes e mede tempo de execução

function buscaBinaria(array, item) {
  let low = 0;
  let high = array.length - 1;
  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    let guess = array[mid];
    if (guess === item) {
      return mid;
    }
  }
}

let start1 = performance.now();
let result1 = buscaBinaria(array, "João");
let end1 = performance.now();

console.log("Resultado da busca binaria: ", result1);
console.log(`T1empo de execução: ${end1 - start1}ms`);