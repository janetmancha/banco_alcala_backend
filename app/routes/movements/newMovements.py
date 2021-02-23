from flask import Flask, request, jsonify
from app.persistencia.MySQL import newMovements, AccountOriginNotExits, TypeMovementsnotExits, NoCredit, AccountsEquals, AccountDestinationNotExits
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
        result = newMovements(data["originAccount"],data["amount"],data["movementType"],destinationAccount)
        return { "originAccount": data["originAccount"]}, 201
    except AccountsEquals as e:
        return {"errorCode":1,"descriptionError":"Cuenta Origen igual a Cuenta Destino"}, 409
    except AccountOriginNotExits as e:
        return {"errorCode":2,"descriptionError":"Cuenta origen no existe"}, 409
    except NoCredit as e:
        return {"errorCode":3,"descriptionError":"Cuenta sin saldo suficiente"}, 409
    except AccountDestinationNotExits as e:
        return {"errorCode":4,"descriptionError":"Cuenta Destino no existe"}, 409
    except TypeMovementsnotExits as e:
        return {"errorCode":5,"descriptionError":"Tipo de movimiento no existe"}, 409
