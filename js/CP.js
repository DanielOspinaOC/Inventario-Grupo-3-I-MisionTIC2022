<<<<<<< HEAD:CP.js
var texto = document.getElementById("Ref");
var boton = document.getElementById("Guardar");

function validarSoloNumeros(){

    let expresion= new RegExp("[0-9]") //Se usa para una variable pero solo se puede usar dentro de la función
    
    if(expresion.test(texto.value)){
        alert("Referencia Correcta")
    }else{
        alert("Hay una o más letras en el campo referencia. Ingrese solo números")
    }
}
boton.addEventListener("click", validarSoloNumeros)
=======
function validarSoloNumeros(){

    let expresion= new RegExp("[0-9]") //Se usa para una variable pero solo se puede usar dentro de la función
    
    if(expresion.test(texto.value)){
        alert("Solamente hay números")
    }else{
        alert("Hay una o más letras")
    }
}
boton.addEventListener("click", validarSoloNumeros)

function actualizar() {
    alert("Se ha modificado la información del producto");
}
>>>>>>> 8a274ceefd79b6c8f7b643cd4051ce2fd996093a:js/CP.js
