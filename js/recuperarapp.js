function validar_correo(){

var correo = RecuperarClave.getElementById("email");

var formatoCorreo = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/;
if(!formatoCorreo.value.match(formatoCorreo))
{
    alert("El correo ingresado es invalido!, ingresa uno correcto..")

    return false;
}
}


function validarForm() {

    var nombre_producto = document.getElementById("nombre_pro");
    var precio_producto = document.getElementById("precio_pro");
    var cantidad_producto = document.getElementById("cant_pro");
    var descripcion_producto = document.getElementById("desc_pro");

    var nom_antiguo = document.getElementById("nom_producto");

    var len_nombre = nombre_producto.value.length;
    var len_precio = precio_producto.value.length;
    var len_cantid = cantidad_producto.value.length;
    var len_descri = descripcion_producto.value.length;

    if (len_nombre == 0 && len_precio == 0 && len_cantid == 0 && len_descri == 0)
    {
        alert("Todos los campos están vacios");
    } else {
        alert("Se ha modificado la información del producto"); // no son campos obligatorios, solo se requiere 1 por lo menos
        document.getElementById("miform").reset();
    }
}

function eliminar() {
    confirm("¿Esta seguro que desea eliminar el producto?");
    document.getElementById("miform").reset();
}
