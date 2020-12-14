var texto = document.getElementById("precio");
var boton = document.getElementById("Guardar");

function validarSoloNumeros(){

    let expresion= new RegExp("[0-9]") //Se usa para una variable pero solo se puede usar dentro de la función
    
    if(expresion.test(texto.value)){
        alert("Precio Correcto")
    }else{
        alert("Hay una o más letras en el campo precio. Ingrese solo números")
    }
}
boton.addEventListener("click", validarSoloNumeros)

function Salir(){
    window.close();
}
Salir.addEventListener("click", Salir)
