from flask import Flask, jsonify, request, redirect
from flask_cors import CORS

## Importamos los files con las funciones de cada módulo
from backend.config.MySQL import database
from backend.routes.usuarios import usuarios_api
from backend.routes.fincas import fincas_api

##from backend.routes.colaborador import *

## Inicializamos el API
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'CONAFFEX'
database.init_app(app)

CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/',methods = ['GET'])
def getInit():
    return jsonify({"Hello":"Nano"})

## Declaramos las rutas requeridas para el API
app.register_blueprint(usuarios_api)
##app.register_blueprint(fincas_api)

if __name__ == "_main_":
   app.run(debug=True)