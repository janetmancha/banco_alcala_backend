from flask import Flask, request, jsonify
from app.persistencia.MySQL import deleteAccount, AccountWithBalance
from app.routes.common import app

@app.route("/api/accounts/<accountNumber>", methods=['DELETE']) 
def delete_account(accountNumber):

    try:
        result = deleteAccount(accountNumber)
    except AccountWithBalance as e:
        print(e)
        return { "message": str(e) }, 409

    if result != None:
        return result, 200
    return { "message": "Cuenta no encontrada" }, 404