from flask import Flask, request, jsonify
from app.persistencia.MySQL import newAccounts
from app.routes.common import app
from mysql.connector import IntegrityError

@app.route("/api/accounts", methods=['POST']) 
def new_Account():
    data = request.get_json()
    try:
        newAccounts(data["accountNumber"],data["dni"],data["accountBalance"])
        return { "accountNumber": data["accountNumber"]}, 201
    except IntegrityError as e:
        if e.errno == 1452:
            return { "message": "El cliente no existe" }, 409
        if e.errno == 1062:
            return { "message": "Cuenta ya existente" }, 409
