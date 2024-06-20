function enviarreclamo(codigo, nombreFormulario) {
    console.log("codigo: " + codigo);
    console.log("codigo.length: " + codigo.length);

    if (codigo.length === 0){
        console.log("codigo vació ");
    }else{
        codigo = "-" + codigo;
    }
    console.log("codigo: " + codigo);
    //OBTENCIÓN DE DATOS DEL FORMULARIO POR ELEMENTOS Y SUS ID
    let nombres = document.getElementById("txt-nombresduda" + codigo).value;
    let sugerencia = document.getElementById("txt-tipoduda" + codigo).value;
    let informacion = document.getElementById("txt-explicacionduda" + codigo).value;

    document.getElementById(nombreFormulario).submit();

}
