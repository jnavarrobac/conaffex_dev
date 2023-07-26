from flask import jsonify
import MySQLdb.cursors
import json

def getAllUsuarios(mysql):
 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM USUARIOS_FEX')
    usuarios = cursor.fetchall()
    
    return jsonify(usuarios)