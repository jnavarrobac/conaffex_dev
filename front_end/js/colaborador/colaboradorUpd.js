
import { dbConfig } from "/config/dbConfig.js";

// ---- DECLARAMOS LOS ELEMENTOS DEL DOM ----

var body = document.getElementsByTagName("body")[0];
body.addEventListener("load", init(), false);

const inputColaboradoresBuscar = document.getElementById('inputBuscarColaboradores');

const tablaColaboradores = document.getElementById("tablaUpdColaboradores");

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
        
        cell6.innerHTML = '<td><button type="button" class="btn btn-inverse-info btn-icon"><i class="mdi mdi-account-settings"></i></button></td>';
        cell6.className = "text-center";

    };
};