let prim = 0
let secon = 0

const print = (args) => console.log(args)

const forLoopTabuada = () => {

    for(prim = 0; prim <= 9; prim++) {
        for(secon = 0; secon <= 9; secon++){
            print(`${prim} X ${secon} = `+ prim * secon)
        }
    }

}

forLoopTabuada()