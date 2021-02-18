from flask import Flask, request, jsonify
from app.persistencia.MySQL import listMovements
from app.routes.common import app

@app.route("/api/movements/<originAccount>", methods=['GET']) 
def list_Movements(originAccount):

    result = listMovements(originAccount)
    
    if len(result) > 0:
        return jsonify(result),200
    return '', 204