from flask import jsonify
import MySQLdb.cursors

def getAllUsuarios(database):
 
    consulta = database.connection.cursor(MySQLdb.cursors.DictCursor)
    consulta.execute('SELECT * FROM USUARIOS_FEX')
    usuarios = consulta.fetchall()
    
    return jsonify(usuarios)

