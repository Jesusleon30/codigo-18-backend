
// como tipado implicito
// que TS interpreta el tipo de dato basado en valor
let nombre = "Hugo" // string

// tipado explicito
let direccion: string = "av mi casa 123"

/**
 * tipos de datos 
 * string
 * number
 * boolean
 * object | null
 * undefined
 */

const numero1: number = 100
const esMayor: boolean = true 
const alumnos: object = []

function sumar (n1:number, n2:number){
    return n1 + n2
}


console.log ("sumando numeros")
console.log(sumar(10,20))



const sumaDeLosProductosDeHoy: number = 100 



