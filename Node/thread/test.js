export function havyOperation() {
  return new Promise((resolve, rejest) => {
    setTimeout(() => {
      resolve('ok')
    }, 5000)
  })
}

console.log('1')
console.log('2')
console.log('3')