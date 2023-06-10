//import { dbConfig } from "/config/dbConfig.js";

// ---- DECLARAMOS LOS ELEMENTOS DEL DOM ----

var body = document.getElementsByTagName("body")[0];
body.addEventListener("load", init(), false);

const inputFechaProduccion    = document.getElementById('campoFechaProduccion');

const selectorFincaProduccion = document.getElementById('selectorFincaProduccion');


function dbConfig() {
    return "http://localhost:5000/";
}

// LA FUNCIÓN DE INICIAR LOS ELEMENTOS Y DATOS NECESARIOS A MOSTRAR CUANDO SE MUESTRE LA PÁGINA
function init() {
   
    // LLAMAMOS LA FUNCIÓN QUE SE ENCARGARÁ DE CARGAR LA LISTA DE FINCAS
    obtenerFincasTotales();

    // LLAMAMOS LA FUNCIÓN QUE OBTIENE LA FECHA ACTUAL PARA SER MOSTRADA
    obtenerFechaActual();
};


// LLAMAMOS LA FUNCIÓN QUE SE ENCARGARÁ DE CARGAR LA LISTA DE FINCAS
function obtenerFincasTotales() {

    const configDB = dbConfig();

    const xhr = new XMLHttpRequest();
    xhr.open('GET', configDB + 'fincas');
    xhr.responseType = 'json';
    xhr.send();

    xhr.onload = function() {
        let response = xhr.response;

        for (var i=0; i<response.length; i++) {

            var option = document.createElement("option");
            option.value = response[i].NUMERO;
            option.text = response[i].NUMERO +" - "+response[i].NOMBRE;            

            selectorFincaProduccion.add(option);
        }; 
    };
};


// LLAMAMOS LA FUNCIÓN QUE OBTIENE LA FECHA ACTUAL PARA SER MOSTRADA
function obtenerFechaActual() {

    let fechaActual = new Date().toLocaleDateString("fr-FR");
    document.getElementById('campoFechaProduccion').value = fechaActual;
  
};