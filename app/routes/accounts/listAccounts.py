from flask import Flask, request, jsonify
from app.persistencia.MySQL import listAccounts
from app.routes.common import app

@app.route("/api/accounts", methods=['GET']) 
def list_Accounts():
    
    dni = request.args.get('filterByDNI')
    
    if dni == None:
        return { "message": "Falta parametro " }, 400

    result = listAccounts(dni)

    if len(result) != 0:
        return jsonify(result), 200
    return { "message": "No existe ninguna cuenta para el dni indicado" }, 404