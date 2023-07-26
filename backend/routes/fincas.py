from flask import Blueprint, render_template, request

## Importamos los files con las funciones de cada módulo
from backend.controller.FincaController import *
from backend.config.MySQL import database

## Instanciamos las rutas de usuarios
fincas_api = Blueprint('fincas_api',__name__)

## 2. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE FINCAS ---- ##

fincas_api.route('/finca',methods = ['POST'])
def registrarFinca():    
    return addFinca(database,request)

fincas_api.route('/fincas',methods = ['GET'])
def obtenerFincas():    
    return getAllFincas(database)

fincas_api.route('/getFincaFiltro',methods = ['POST'])
def obtenerFinca():    
    return getFincaFiltro(database,request)

fincas_api.route('/getOneFinca',methods = ['POST'])
def obtenerOneFinca():    
    return getOneFinca(database,request)

fincas_api.route('/finca',methods = ['PUT'])
def actualizarFinca():    
    return updateFinca(database,request)

## 2. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE FINCAS ---- ##