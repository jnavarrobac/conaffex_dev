from flask import jsonify
import MySQLdb.cursors
import json

def getAllFincas(mysql):
 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT A.*, B.IDENTIFICACION, B.NOMBRE AS PROPIETARIO FROM FINCAS_FEX AS A INNER JOIN USUARIOS_FEX AS B ON A.NUM_PROPIETARIO = B.NUMERO')
    fincas = cursor.fetchall()
    
    return jsonify(fincas)

def getFincaFiltro(mysql,request):
 
    finca = ''
    datoIngresado = json.loads(request.data)

    if request.method == 'POST' and 'datoIngresado' in datoIngresado:
       dato = datoIngresado["datoIngresado"]      
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute("SELECT A.*, B.IDENTIFICACION, B.NOMBRE AS PROPIETARIO FROM FINCAS_FEX AS A INNER JOIN USUARIOS_FEX AS B ON A.NUM_PROPIETARIO = B.NUMERO WHERE A.NUMERO LIKE '%"+dato+"%' OR A.NOMBRE LIKE '%"+dato+"%'")
       finca = cursor.fetchall()
       msg = 'Se ha encontrado el colaborador con éxito!'
    
    elif request.method == 'POST':
       msg = 'No se ha encontrado ningún colaborador!'

    return jsonify(finca)

def getOneFinca(mysql,request):
 
    finca = ''
    datoIngresado = json.loads(request.data)

    if request.method == 'POST' and 'datoIngresado' in datoIngresado:
       dato = datoIngresado["datoIngresado"]      
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       sql_select_query = """SELECT A.*, B.IDENTIFICACION, B.NOMBRE AS PROPIETARIO FROM FINCAS_FEX AS A INNER JOIN USUARIOS_FEX AS B ON A.NUM_PROPIETARIO = B.NUMERO WHERE A.NUMERO = %s"""
       cursor.execute(sql_select_query, (dato,))
       finca = cursor.fetchall()
       msg = 'Se ha encontrado el colaborador con éxito!'
    
    elif request.method == 'POST':
       msg = 'No se ha encontrado ningún colaborador!'

    return jsonify(finca)

def updateFinca(mysql,request):

    msg = ''
    datosActualizar = json.loads(request.data)
   
    if request.method == 'PUT' and 'numeroFinca' in datosActualizar and 'nombreCompleto' in datosActualizar and 'tamano' in datosActualizar and 'ubicacion' in datosActualizar and 'numeroPropietario' in datosActualizar:
       numeroFinca    = datosActualizar["numeroFinca"]
       nombreCompleto = datosActualizar["nombreCompleto"]
       tamano         = datosActualizar["tamano"]
       ubicacion      = datosActualizar["ubicacion"]
       numeroPropietario = datosActualizar["numeroPropietario"]

       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute("UPDATE FINCAS_FEX SET NOMBRE = %s, TAMANO = %s, UBICACION = %s, NUM_PROPIETARIO = %s WHERE NUMERO = %s",
                     (nombreCompleto, tamano, ubicacion, numeroPropietario,numeroFinca))
       mysql.connection.commit()
       msg = 'Se ha actualizado la finca con éxito!'
    
    elif request.method == 'PUT':
        msg = 'Por favor ingresar los datos solicitados!'
    
    return jsonify(msg)