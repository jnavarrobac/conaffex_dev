from flask import Blueprint, render_template

## Importamos los files con las funciones de cada módulo
from backend.controller.UsuarioController import *
from backend.config.MySQL import database

## Instanciamos las rutas de usuarios
usuarios_api = Blueprint('usuarios_api',__name__)

## 3. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE USUARIOS ---- ##

@usuarios_api.route('/usuarios',methods = ['GET'])
def obtenerUsuarios():    
    return getAllUsuarios(database)

## 3. ---- DECLARAMOS LAS RUTAS DE FUNCIÓN DE USUARIOS ---- ##