
function Salir(){
    window.close();
}

Salir.addEventListener("click", Salir)


var texto = document.getElementById("Ref");
var texto = document.getElementById("Precio");
var texto = document.getElementById("Cantidad");
var boton = document.getElementById("Guardar");


function validarSoloNumerosRef(){

    let expresion= new RegExp("[0-9]") //Se usa para una variable pero solo se puede usar dentro de la función
    
    if(expresion.test(texto.value)){
        alert("Referencia Correcta")
    }else{
        alert("Hay una o más letras en el campo referencia. Ingrese solo números")
    }
}

boton.addEventListener("click", validarSoloNumerosRef)


function validarSoloNumerosPrecio(){

    let expresion= new RegExp("[0-9]") //Se usa para una variable pero solo se puede usar dentro de la función
    
    if(expresion.test(texto.value)){
        alert("Referencia Correcta")
    }else{
        alert("Hay una o más letras en el campo precio. Ingrese solo números")
    }
}

boton.addEventListener("click", validarSoloNumerosPrecio)