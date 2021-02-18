import unittest
from app.routes.common import app
from app.persistencia.MySQL import insertCustomer, deleteCustomer, newAccounts, newMovements

class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

        insertCustomer('1234J','Janet','pass1')
        insertCustomer('1234G','German','pass2')
        insertCustomer('1234H','Hugo','pass3')
        insertCustomer('1234P','Pili','pass4')
        insertCustomer('1234M','Manoli','pass5')

        newAccounts(1,'1234J',1200)
        newAccounts(2,'1234G',1000)
        newAccounts(3,'1234G',400)
        newAccounts(4,'1234P',2000)
        newAccounts(5,'1234M',2000)
        newAccounts(6,'1234J',0)

        newMovements(4,2000,'deposit',0)
        newMovements(4,100,'withdrawn',0)
        newMovements(4,500,'transfer',1)
        
    def tearDown(self):
        # deleteCustomerTest()
        deleteCustomer('1234J')
        deleteCustomer('1234G')
        deleteCustomer('1234P')
        deleteCustomer('1234H')
        deleteCustomer('1234V')
        deleteCustomer('1234M')