let ajax = new XMLHttpRequest();

function ajaxVerify() {
    
    ajax.addEventListener("readystatechange", () => {
        if (ajax.readyState === 4 && ajax.status == 200) {
            const ul = document.querySelector('.list')
            const resposta = ajax.response
            
            ul.innerHTML += `
                <li>${resposta.name}</li>
                <li>${resposta.version}</li>
                <li>${resposta.main}</li>
                <li>${resposta.scripts.test}</li>
                <li>${resposta.license}</li>
            `
            
        }
    })
}

function jsonAPI(){
    ajax.responseType = 'json'

    ajax.open('GET', 'components/main.json', true)
    ajax.send()

    ajaxVerify()
}

$(".btn").click(() => {
    jsonAPI()
})


