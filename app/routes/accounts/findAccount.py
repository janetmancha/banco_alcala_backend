from flask import Flask, request, jsonify
from app.persistencia.MySQL import findAccount
from app.routes.common import app

@app.route("/api/accounts/<accountNumber>", methods=['GET']) 
def find_account(accountNumber):
    result = findAccount(accountNumber)
  
    if result != None:
        return result
    return { "message": "No encontrado" }, 404