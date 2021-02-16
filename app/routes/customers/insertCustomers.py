from flask import Flask, request, jsonify
from app.persistencia.MySQL import insertCustomer
from app.routes.common import app
from mysql.connector import IntegrityError

@app.route("/api/customers", methods=['POST']) 
def insert_Customer():
    data = request.get_json()
    try:
        insertCustomer(data["dni"],data["name"],data["password"])
        return { "dni": data["dni"]}, 201
    except IntegrityError as e:
        return { "message": "Cliente duplicado" }, 409