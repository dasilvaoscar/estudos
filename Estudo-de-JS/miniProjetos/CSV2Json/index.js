const file = document.getElementById('form-file')

function readCSV(){
    document.getElementById('send-buttom').addEventListener('click', () => {
        alert(file.value)
    })

}
