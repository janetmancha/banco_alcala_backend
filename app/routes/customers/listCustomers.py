from flask import Flask, request, jsonify
from app.persistencia.MySQL import listCustomers
from app.routes.common import app

@app.route("/api/customers", methods=['GET']) 
def list_Customers():
    result = listCustomers()
    if len(result) > 0:
        return jsonify(result),200
    return '', 204