from flask import Flask, request, jsonify
from app.persistencia.MySQL import deleteCustomer
from app.routes.common import app

@app.route("/api/customers/<dni>", methods=['DELETE']) 
def delete_customer(dni):

    result = deleteCustomer(dni)
    if result > 0:
        return { "message": "cliente borrado"}, 201
    else:
        return { "message": "No encontrado" }, 404