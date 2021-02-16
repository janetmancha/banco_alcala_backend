from flask import Flask, request, jsonify
from app.persistencia.MySQL import findCustomer
from app.routes.common import app

@app.route("/api/customers/<dni>", methods=['GET']) 
def find_customer(dni):
    result = findCustomer(dni)
  
    if result != None:
        return result
    return { "message": "No encontrado" }, 404
