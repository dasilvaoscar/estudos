
async function outra() {
  return await 'Ok'
}

async function a() {
  console.log('1')
  console.log('2')
  console.log('3')
  console.log(outra())
}

a()