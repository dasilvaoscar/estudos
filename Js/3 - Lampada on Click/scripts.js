const lampada_on = '../img/lampada-on.jpg'
const lampada_off =  '../img/lampada-off.jpg'
const body = document.body

body.innerHTML = `<img src="${lampada_off}" id='lampada' alt="" srcset="">`
const lampada = document.getElementById('lampada')
lampada.setAttribute('onclick', 'getLampada()')


function getLampada(){    

    const lampada_stage = lampada.getAttribute('src')
    if(lampada_stage == lampada_off) 
        lampada.setAttribute('src', lampada_on)
    else 
        lampada.setAttribute('src', lampada_off)

}