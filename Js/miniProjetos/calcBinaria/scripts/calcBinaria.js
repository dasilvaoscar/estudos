function dis(val) { 
    document.getElementById("result").value+=val 
} 
  
function clr() { 
    document.getElementById("result").value = "" 
} 


const CalcBin = () => {
    let number = document.getElementById("result").value 
    let resto = []

    while(number != 1){
        resto.push(number % 2);
        number = Math.trunc(number / 2);
        if (number == 1){
            break
        }
    }
    
    resto.reverse()
    result = String(resto).replace(/,/g,'')
    //return `Em BINÁRIO: 1${result}`
    return document.getElementById("result").value = `1${result}`
}
