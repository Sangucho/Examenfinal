function enviarcompra(codigo, nombreFormulario) {
    console.log("codigo: " + codigo);
    console.log("codigo.length: " + codigo.length);

    if (codigo.length === 0){
        console.log("codigo vació ");
    }else{
        codigo = "-" + codigo;
    }
    console.log("codigo: " + codigo);
    //OBTENCIÓN DE DATOS DEL FORMULARIO POR ELEMENTOS Y SUS ID
    let norden = document.getElementById("txt-tipo-pago" + codigo).value;
    let mpagado = document.getElementById("txt-monto-pagado" + codigo).value;
    let mpago = document.getElementById("txt-nro-orden" + codigo).value;

    document.getElementById(nombreFormulario).submit();

}
