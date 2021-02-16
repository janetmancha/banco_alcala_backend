from . import BaseTestClass
import json 
from flask import jsonify


class TestEndPointCustomer (BaseTestClass):

    def test_list_customers(self):
        res = self.client.get('/api/customers')
        self.assertEqual(200, res.status_code)

        resDict = json.loads(res.data) #convertir un json en diccionario o a una lista de python
        # print(resDict)
       
        #comprobar si janet y german están en el diccionario creado
        assert({'dni': '1234J', 'name': 'Janet', 'password': 'pass1'} in resDict)
        assert({'dni': '1234G', 'name': 'German', 'password': 'pass2'} in resDict)

    def test_new_customer(self):
        res = self.client.post('/api/customers',json={"dni": "1234V", "name": "Varas", "password": "pass5"})
        self.assertEqual(201, res.status_code)
        res = self.client.post('/api/customers',json={"dni": "1234V", "name": "Varas", "password": "pass5"})
        self.assertEqual(409, res.status_code)

    def test_find_customer(self):
        res = self.client.get('/api/customers/1234H')
        self.assertEqual(200, res.status_code)

        res = self.client.get('api/customers/1234Z')
        self.assertEqual(404, res.status_code)   

    def test_delete_customer(self):
        res = self.client.delete('/api/customers/1234P')
        self.assertEqual(201, res.status_code)

        res = self.client.delete('api/customers/1234Z')
        self.assertEqual(404, res.status_code)     
    