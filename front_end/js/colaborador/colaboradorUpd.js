
//import { dbConfig } from "/config/dbConfig.js";

// ---- DECLARAMOS LOS ELEMENTOS DEL DOM ----

var body = document.getElementsByTagName("body")[0];
body.addEventListener("load", init(), false);

const inputColaboradoresBuscar      = document.getElementById('inputBuscarColaboradores');
const inputNombreActualizar         = document.getElementById('campoNombreActualizar');
const inputIdentificacionActualizar = document.getElementById('campoIdentificacionActualizar');
const inputTelefonoActualizar       = document.getElementById('campoTelefonoActualizar');
const inputTarjetaActualizar        = document.getElementById('campoTarjetaActualizar');

const tablaColaboradores = document.getElementById("tablaUpdColaboradores");

const selectorGeneroActualizar = document.getElementById('selectorGeneroActualizar');
const selectorTipoActualizar   = document.getElementById('selectorTipoActualizar');

const seccionActualizarColaborador       = document.getElementById('seccionActualizarColaborador');
const seccionTablaActualizarColaborador  = document.getElementById('seccionTablaActualizarColaborador');

const botonActualizar = document.getElementById('buttonActualizar');
const botonAtras      = document.getElementById('buttonAtras');

function dbConfig() {
    return "http://localhost:5000/";
}

// LLAMAMOS LA FUNCIÓN QUE TRAE LA LISTA DE COLABORADORES
// EN EL MOMENTO QUE SE CREA LA VENTANA
function init() {

    const configDB = dbConfig();

    const xhr = new XMLHttpRequest();
    xhr.open('GET', configDB + 'colaboradores');
    xhr.responseType = 'json';
    xhr.send();

    xhr.onload = function() {
        let response = xhr.response;
        setColaboradoresTabla(response); 
    };
};

// DECLARAMOS FUNCION PARA COMPLETAR LA TABLA 
// CON LA LISTA DE COLABORADORES

function setColaboradoresTabla(data){
    
    // LIMPIAMOS LA TABLA EN CADA LLAMADA DE ACTUALIZACIÓN
    while(tablaColaboradores.rows.length > 1) {
          tablaColaboradores.deleteRow(1);
    }
    // Se recorre la lista de colaboradores que devuelve la base de datos, para ingresarlas a la tabla

    for (var i=0; i<data.length; i++) {
    
        var row = tablaColaboradores.insertRow(i+1);

        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);
        var cell6 = row.insertCell(5);

        cell1.innerHTML = data[i].NUMERO;
        cell1.className = "text-center";
        
        cell2.innerHTML = data[i].NOMBRE;
        cell2.className = "text-center";

        cell3.innerHTML = data[i].IDENTIFICACION;
        cell3.className = "text-center";

        cell4.innerHTML = data[i].TELEFONO;
        cell4.className = "text-center";

        cell5.innerHTML = data[i].NUM_TARJETA;
        cell5.className = "text-center";
        
        cell6.innerHTML = "<td><button type='button' class='btn btn-inverse-info btn-icon' onclick=seleccionarColaborador("+data[i].NUMERO+");><i class='mdi mdi-account-settings'></i></button></td>";
        cell6.className = "text-center";

    };
};

// DECLARAMOS FUNCION PARA COMPLETAR FILTRAR COLABORADORES SEGÚN EL BUSCADOR 

inputColaboradoresBuscar.addEventListener('keyup', function(){
    
    const configDB = dbConfig();

    const xhr = new XMLHttpRequest();
    const body = JSON.stringify({"datoIngresado": inputColaboradoresBuscar.value} );
    xhr.open('POST', configDB + 'getColaboradorFiltro');
    xhr.responseType = 'json';
    xhr.send(body);

    xhr.onload = function() {
        let response = xhr.response;
        setColaboradoresTabla(response); 
    };

});

// DECLARAMOS FUNCION PARA SELECCIONAR EL COLABORADOR A ACTUALIZAR
function seleccionarColaborador(numeroColaborador){

    //ESCONDEMOS LA TABLA DE COLABORADORES Y MOSTRAMOS EL PANEL DE ACTUALIZAR
    seccionTablaActualizarColaborador.style.display = "none";
    seccionActualizarColaborador.style.display = "block"

    const configDB = dbConfig();

    const xhr = new XMLHttpRequest();
    const body = JSON.stringify({"datoIngresado": numeroColaborador} );
    xhr.open('POST', configDB + 'getOneColaborador');
    xhr.responseType = 'json';
    xhr.send(body);

    xhr.onload = function() {
        let response = xhr.response; 

        inputNombreActualizar.value = response[0].NOMBRE;
        inputIdentificacionActualizar.value = response[0].IDENTIFICACION;
        inputTarjetaActualizar.value = response[0].NUM_TARJETA;
        inputTelefonoActualizar .value = response[0].TELEFONO; 
    };

};


botonAtras.addEventListener('click', function(){
    
    //MOSTRAMOS LA TABLA DE COLABORADORES Y ESCONDEMOS EL PANEL DE ACTUALIZAR
    seccionTablaActualizarColaborador.style.display = "block";
    seccionActualizarColaborador.style.display = "none"

});
