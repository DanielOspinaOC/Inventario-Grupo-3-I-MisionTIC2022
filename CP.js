function validarSoloNumeros(){

    let expresion= new RegExp("[0-9]") //Se usa para una variable pero solo se puede usar dentro de la función
    
    if(expresion.test(texto.value)){
        alert("Solamente hay números")
    }else{
        alert("Hay una o más letras")
    }
}
boton.addEventListener("click", validarSoloNumeros)