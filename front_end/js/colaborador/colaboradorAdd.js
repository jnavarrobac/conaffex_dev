//import { dbConfig } from "/config/dbConfig.js";

// ---- DECLARAMOS LOS ELEMENTOS DEL DOM ----

const inputNombreAgregar         = document.getElementById('campoNombreAgregar');
const inputIdentificacionAgregar = document.getElementById('campoIdentificacionAgregar');
const inputTelefonoAgregar       = document.getElementById('campoTelefonoAgregar');
const inputTarjetaAgregar        = document.getElementById('campoTarjetaAgregar');
const inputObservacionesAgregar  = document.getElementById('campoObservacionesAgregar');

const selectorGeneroAgregar = document.getElementById('selectorGeneroAgregar');
const selectorTipoAgregar = document.getElementById('selectorTipoAgregar');

const botonAgregar  = document.getElementById('buttonAgregar');
const botonCancelar = document.getElementById('buttonCancelar');

function dbConfig() {
    return "http://localhost:5000/";
}

// DECLARAMOS LA FUNCIÓN QUE SE ENCARGA DE ALMACENAR UN NUEVO COLABORADOR
botonAgregar.addEventListener('click', function(){
       
    const configDB = dbConfig();

    const xhr = new XMLHttpRequest();
    xhr.open("POST", configDB + "colaborador");
    const body = JSON.stringify({"nombreCompleto": inputNombreAgregar.value, "identificacion": inputIdentificacionAgregar.value, "tarjeta": inputTarjetaAgregar.value, "telefono": inputTelefonoAgregar.value, "observaciones": inputObservacionesAgregar.value, "tipo": selectorTipoAgregar.value, "genero": selectorGeneroAgregar.value } );

    xhr.onload = () => {
    
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(JSON.parse(xhr.responseText));
            botonCancelar.click();
        } else {
            console.log(`Error: ${xhr.status}`);
        }
    };

    xhr.send(body);
});

// ACCIÓN PARA LIMPIAR LOS CAMPOS DE AGREGAR COLABORADOR
botonCancelar.addEventListener('click', function(){
       
    inputNombreAgregar.value = "";
    inputIdentificacionAgregar.value = "";
    inputTelefonoAgregar.value = "";
    inputTarjetaAgregar.value  = "";
    inputObservacionesAgregar.value  = "";
   
});