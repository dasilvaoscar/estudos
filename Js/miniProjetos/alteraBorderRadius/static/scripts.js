const p = document.getElementById('rcorners1')

const personalBorder = () => {    
    const input = document.getElementById('input-borda')
    p.style.borderRadius = `${input.value}px`
}

const personalWidth = () => {
    const input = document.getElementById('input-tamanho')
    p.style.width = `${input.value}px`
}

const personalHeight = () => {
    const input = document.getElementById('input-altura')
    p.style.height = `${input.value}px`
}
