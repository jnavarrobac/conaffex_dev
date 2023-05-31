from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

## Importamos los files con las funciones de cada módulo
from backend.routes.colaborador import *
from backend.routes.fincas import *
from backend.routes.usuarios import *

app = Flask(__name__)

CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'CONAFFEX'

mysql = MySQL(app)

@app.route('/',methods = ['GET'])
def getInit():
    return jsonify({"Hello":"Nano"})

## 1. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE COLABORADOR ---- ##

@app.route('/colaborador',methods = ['POST'])
def registrarColaborador():    
    return addColaborador(mysql,request)

@app.route('/colaboradores',methods = ['GET'])
def obtenerColaboradores():    
    return getAllColaboradores(mysql)

@app.route('/getColaboradorFiltro',methods = ['POST'])
def obtenerColaborador():    
    return getColaboradorFiltro(mysql,request)

@app.route('/getOneColaborador',methods = ['POST'])
def obtenerOneColaborador():    
    return getOneColaborador(mysql,request)

@app.route('/colaborador',methods = ['PUT'])
def actualizarColaborador():    
    return updateColaborador(mysql,request)

## 1. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE COLABORADOR ---- ##

## 2. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE FINCAS ---- ##

@app.route('/finca',methods = ['POST'])
def registrarFinca():    
    return addFinca(mysql,request)

@app.route('/fincas',methods = ['GET'])
def obtenerFincas():    
    return getAllFincas(mysql)

@app.route('/getFincaFiltro',methods = ['POST'])
def obtenerFinca():    
    return getFincaFiltro(mysql,request)

@app.route('/getOneFinca',methods = ['POST'])
def obtenerOneFinca():    
    return getOneFinca(mysql,request)

@app.route('/finca',methods = ['PUT'])
def actualizarFinca():    
    return updateFinca(mysql,request)

## 2. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE FINCAS ---- ##

## 3. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE USUARIOS ---- ##

@app.route('/usuarios',methods = ['GET'])
def obtenerUsuarios():    
    return getAllUsuarios(mysql)

## 3. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE USUARIOS ---- ##

if __name__ == "_main_":
   app.run(debug=True)