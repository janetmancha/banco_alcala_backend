from . import BaseTestClass
import json 
from flask import jsonify

class TestEndPointAccount (BaseTestClass):

    def test_new_account(self):
        res = self.client.post('/api/accounts',json={"accountNumber": 15, "dni": "1234M", "accountBalance": 1000})
        self.assertEqual(201, res.status_code)
        
        res = self.client.post('/api/accounts',json={"accountNumber": 15, "dni": "1234M", "accountBalance": 1200})
        self.assertEqual(409, res.status_code)
        
        res = self.client.post('/api/accounts',json={"accountNumber": 20, "dni": "1234W", "accountBalance": 200})
        self.assertEqual(409, res.status_code)

    def test_list_accounts(self):
        res = self.client.get('/api/accounts?filterByDNI=1234G')
        self.assertEqual(200, res.status_code)

        resDict = json.loads(res.data) #convertir un json en diccionario o a una lista de python
       
        # comprobar si las cuentas german están en el diccionario creado
        assert({'accountNumber': 2, 'dni': '1234G', 'accountBalance': 1000} in resDict)
        assert({'accountNumber': 3, 'dni': '1234G', 'accountBalance': 400} in resDict)

    def test_find_account(self):
        res = self.client.get('/api/accounts/1')
        self.assertEqual(200, res.status_code)

        res = self.client.get('/api/accounts/25')
        self.assertEqual(404, res.status_code)

    def test_delete_account(self):
        res = self.client.delete('/api/accounts/6')
        self.assertEqual(200, res.status_code)

        res = self.client.delete('/api/accounts/3')
        self.assertEqual(409, res.status_code)

        res = self.client.delete('api/customers/200')
        self.assertEqual(404, res.status_code) 

