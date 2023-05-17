from flask import jsonify
import MySQLdb.cursors
import json

def addColaborador(mysql,request):
    
    msg = ''
    datosIngresar = json.loads(request.data)

    if request.method == 'POST' and 'nombreCompleto' in datosIngresar and 'identificacion' in datosIngresar and 'tarjeta' in datosIngresar and 'telefono' in datosIngresar and 'observaciones' in datosIngresar and 'tipo' in datosIngresar and 'genero' in datosIngresar:
       nombreCompleto = datosIngresar["nombreCompleto"]
       identificacion = datosIngresar["identificacion"]
       tarjeta        = datosIngresar["tarjeta"]
       telefono       = datosIngresar["telefono"]
       observaciones  = datosIngresar["observaciones"]
       tipo           = datosIngresar["tipo"]
       genero         = datosIngresar["genero"]

       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('INSERT INTO COLABORADOR_FEX VALUES (NULL, % s, % s, % s, % s, % s, % s, % s)', (nombreCompleto,identificacion,telefono,tarjeta,observaciones,tipo,genero, ))
       mysql.connection.commit()
       msg = 'Se ha creado un colaborador con éxito!'
    
    elif request.method == 'POST':
        msg = 'Por favor ingresar los datos solicitados!'
    
    return jsonify(msg)


def getAllColaboradores(mysql):
 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM COLABORADOR_FEX')
    colaboradores = cursor.fetchall()
    
    return jsonify(colaboradores)


def getColaboradorFiltro(mysql,request):
 
    colaborador = ''
    datoIngresado = json.loads(request.data)

    if request.method == 'POST' and 'datoIngresado' in datoIngresado:
       dato = datoIngresado["datoIngresado"]      
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute("SELECT * FROM COLABORADOR_FEX WHERE NUMERO LIKE '%"+dato+"%' OR NOMBRE LIKE '%"+dato+"%'")
       colaborador = cursor.fetchall()
       msg = 'Se ha encontrado el colaborador con éxito!'
    
    elif request.method == 'POST':
       msg = 'No se ha encontrado ningún colaborador!'

    return jsonify(colaborador)

def getOneColaborador(mysql,request):
 
    colaborador = ''
    datoIngresado = json.loads(request.data)

    if request.method == 'POST' and 'datoIngresado' in datoIngresado:
       dato = datoIngresado["datoIngresado"]      
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       sql_select_query = """SELECT * FROM COLABORADOR_FEX WHERE NUMERO = %s"""
       cursor.execute(sql_select_query, (dato,))
       colaborador = cursor.fetchall()
       msg = 'Se ha encontrado el colaborador con éxito!'
    
    elif request.method == 'POST':
       msg = 'No se ha encontrado ningún colaborador!'

    return jsonify(colaborador)

def updateColaborador(mysql,request):

    msg = ''
    datosActualizar = json.loads(request.data)

    if request.method == 'PUT' and 'numeroColaborador' in datosActualizar and 'nombreCompleto' in datosActualizar and 'identificacion' in datosActualizar and 'tarjeta' in datosActualizar and 'telefono' in datosActualizar and 'observaciones' in datosActualizar and 'tipo' in datosActualizar and 'genero' in datosActualizar:
       numeroColaborador = datosActualizar["numeroColaborador"]
       nombreCompleto = datosActualizar["nombreCompleto"]
       identificacion = datosActualizar["identificacion"]
       tarjeta        = datosActualizar["tarjeta"]
       telefono       = datosActualizar["telefono"]
       observaciones  = datosActualizar["observaciones"]
       tipo           = datosActualizar["tipo"]
       genero         = datosActualizar["genero"]

       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute("UPDATE COLABORADOR_FEX SET NOMBRE = %s, IDENTIFICACION = %s, TELEFONO = %s, NUM_TARJETA = %s, OBSERVACIONES = %s,TIPO = %s,GENERO = %s WHERE NUMERO = %s",
                     (nombreCompleto, identificacion, telefono, tarjeta, observaciones,tipo,genero,numeroColaborador))
       mysql.connection.commit()
       msg = 'Se ha actualizado el colaborador con éxito!'
    
    elif request.method == 'PUT':
        msg = 'Por favor ingresar los datos solicitados!'
    
    return jsonify(msg)
