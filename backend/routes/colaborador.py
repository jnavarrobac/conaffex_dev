from flask import Flask, jsonify, request

## Importamos los files con las funciones de cada módulo
from backend.controller.ColaboradorController import *
from backend.config.MySQL import *

app = Flask(__name__)

## LLAMAMOS LA INSTANCIA DE LA BASE DE DATOS ## 

conexionBaseDatos = obtenterInstanciaDB(app)

## 1. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE COLABORADOR ---- ##

@app.route('/colaborador',methods = ['POST'])
def registrarColaborador():    
    return addColaborador(conexionBaseDatos,request)

@app.route('/colaborador',methods = ['GET'])
def obtenerColaboradores():    
    return getAllColaboradores(conexionBaseDatos)

@app.route('/colaboradorfiltro/<valor>',methods = ['GET'])
def obtenerColaborador(valor):    
    return getColaboradorFiltro(conexionBaseDatos,request,valor)

@app.route('/getOneColaborador',methods = ['POST'])
def obtenerOneColaborador():    
    return getOneColaborador(conexionBaseDatos,request)

@app.route('/colaborador',methods = ['PUT'])
def actualizarColaborador():    
    return updateColaborador(conexionBaseDatos,request)

## 1. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE COLABORADOR ---- ##
