//import { dbConfig } from "/config/dbConfig.js";

// ---- DECLARAMOS LOS ELEMENTOS DEL DOM ----

var body = document.getElementsByTagName("body")[0];
body.addEventListener("load", init(), false);

const tablaFincas = document.getElementById("tablaUpdFincas");

function dbConfig() {
    return "http://localhost:5000/";
}

// LLAMAMOS LA FUNCIÓN QUE TRAE LA LISTA DE FINCAS
// EN EL MOMENTO QUE SE CREA LA VENTANA
function init() {

    const configDB = dbConfig();

    const xhr = new XMLHttpRequest();
    xhr.open('GET', configDB + 'fincas');
    xhr.responseType = 'json';
    xhr.send();

    xhr.onload = function() {
        let response = xhr.response;
        setFincasTabla(response); 
    };
};

// DECLARAMOS FUNCION PARA COMPLETAR LA TABLA 
// CON LA LISTA DE COLABORADORES

function setFincasTabla(data){
    
    // LIMPIAMOS LA TABLA EN CADA LLAMADA DE ACTUALIZACIÓN
    while(tablaFincas.rows.length > 1) {
          tablaFincas.deleteRow(1);
    }
    // Se recorre la lista de colaboradores que devuelve la base de datos, para ingresarlas a la tabla

    for (var i=0; i<data.length; i++) {
    
        var row = tablaFincas.insertRow(i+1);

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

        cell3.innerHTML = data[i].TAMANO;
        cell3.className = "text-center";

        cell4.innerHTML = data[i].UBICACION;
        cell4.className = "text-center";

        cell5.innerHTML = data[i].IDENTIFICACION +' - '+ data[i].PROPIETARIO;
        cell5.className = "text-center";
        
        cell6.innerHTML = "<td><button type='button' class='btn btn-inverse-danger btn-icon' onclick=seleccionarColaborador("+data[i].NUMERO+");><i class='mdi mdi-image-multiple'></i></button></td>";
        cell6.className = "text-center";

    };
};