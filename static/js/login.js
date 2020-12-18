function validarLogin()
{
    var usuario = document.getElementById("user");
    var contrasena = document.getElementById("contrasena");

    var len_usuario = usuario.value.length;
    

    if (len_usuario == 0 || len_usuario > 8) 
    {
        alert("El usuario debe contener mínimo 8 caracteres")
    
        return false;
    }
    if(expresion.test(usuario.value)){
        
    }else{
        alert("El usuario es el numero de cedula, por favor ingrese solo numeros")
    }
}

function mostrarPassword() 
{
    var obj = document.getElementById('password');
    obj.type = "text";
}

function ocultarPassword() {
    var obj = document.getElementById('password');
    obj.type="password";
}