function enviarsugerencia(codigo, nombreFormulario) {
    console.log("codigo: " + codigo);
    console.log("codigo.length: " + codigo.length);

    if (codigo.length === 0){
        console.log("codigo vació ");
    }else{
        codigo = "-" + codigo;
    }
    console.log("codigo: " + codigo);
    //OBTENCIÓN DE DATOS DEL FORMULARIO POR ELEMENTOS Y SUS ID
    let nombres = document.getElementById("txt-nombressugerencia" + codigo).value;
    let sugerencia = document.getElementById("txt-tiposugerencia" + codigo).value;
    let informacion = document.getElementById("txt-masinformacion" + codigo).value;

    document.getElementById(nombreFormulario).submit();

}
