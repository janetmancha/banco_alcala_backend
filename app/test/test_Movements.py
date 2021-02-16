from . import BaseTestClass
import json 
from flask import jsonify


class TestEndPointMovement (BaseTestClass):

    def test_list_movements(self):
        res = self.client.get('/api/movements/4')
        self.assertEqual(200, res.status_code)

        #convertir un json en diccionario o a una lista de python
        resDict = json.loads(res.data) 
       
        res = self.client.get('/api/movements/2')
        self.assertEqual(204, res.status_code)
