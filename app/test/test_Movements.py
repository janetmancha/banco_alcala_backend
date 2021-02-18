from . import BaseTestClass
import json 
from flask import jsonify

class TestEndPointMovement (BaseTestClass):

    def test_list_movements(self):
        res = self.client.get('/api/movements/4')
        self.assertEqual(200, res.status_code)

        # convertir un json en lista de diccionario de python
        resDict = json.loads(res.data) 
        # filtrar la lista de diccionario con los campos que necesitamos
        result= [ {"originAccount": x["originAccount"],"amount": x["amount"],"movementType":x["movementType"],"destinationAccount":x["destinationAccount"] } for x in resDict ]

        # comprobar si los siguiente movimientos están en el diccionario creado
        assert({'originAccount': 4, 'amount': 2000, 'destinationAccount': 0, 'movementType': 'deposit'} in result)
        assert({'originAccount': 4, 'amount': 100, 'destinationAccount': 0, 'movementType': 'withdrawn'} in result)
        assert({'originAccount': 4, 'amount': 500, 'destinationAccount': 1, 'movementType': 'transfer'} in result)

        res = self.client.get('/api/movements/1')
        self.assertEqual(200, res.status_code)
