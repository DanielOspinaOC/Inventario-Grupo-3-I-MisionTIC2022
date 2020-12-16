function validar_correo(){

var correo = RecuperarClave.getElementById("email");

var formatoCorreo = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/;
if(!formatoCorreo.value.match(formatoCorreo))
{
    alert("El correo ingresado es invalido!, ingresa uno correcto..")

    return false;
}
}
