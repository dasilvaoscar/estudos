// Exploran do o objeto Window

const confirm = window.confirm('Deseja escreve algum texto ?')
const text = null

if(confirm == true){
    text = window.prompt('Digite um texto !')
    window.alert(text)
}
else{
    window.alert('Usuário não informou texto')
}

// O metodo alert pode ser abreviado 
alert("Olá\nComo vai voçe ?");