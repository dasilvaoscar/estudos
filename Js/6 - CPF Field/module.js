const cpf = document.getElementById('cpf') 
const mensage = () => {
    window.alert(`${cpf.value.substr(0, 3)}.${cpf.value.substr(3, 3)}.${cpf.value.substr(6, 3)}-${cpf.value.substr(9, 2)}`)
}