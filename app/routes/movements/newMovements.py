from flask import Flask, request, jsonify
from app.persistencia.MySQL import newMovements
from app.routes.common import app
from mysql.connector import IntegrityError
from mysql.connector import Error
from mysql.connector import errorcode

@app.route("/api/movements", methods=['POST']) 
def new_Movement():
    data = request.get_json()
    
    destinationAccount = 0

    if "destinationAccount" in data:
        destinationAccount = data["destinationAccount"]

    try:
        result = newMovements(data["originAccount"],data["amount"],data["movementType"])
        return { "originAccount": data["originAccount"]}, 201
    except IntegrityError as e:
        return { "message": "El cliente no existe" }, 409
