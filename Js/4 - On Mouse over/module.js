// Global const
const img = document.getElementById('imgClass')
const on = 'https://github.com/gabrieldarezzo/helpjs-ravi/blob/master/images/lampada-on.jpg?raw=true'
const off = 'https://github.com/gabrieldarezzo/helpjs-ravi/blob/master/images/lampada.jpg?raw=true'

// Arrow Func
const lampada_off = () => {if(img.getAttribute('src') == on){img.setAttribute('src', off)}}
const lampada_on = () => {if(img.getAttribute('src') == off){img.setAttribute('src', on)}}