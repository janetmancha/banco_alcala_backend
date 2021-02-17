import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

class AccountWithBalance (Exception):
    pass

class AccountnotExits (Exception):
    pass

class TypeMovementsnotExits (Exception):
    pass

conexion = None
cursor = None

def crearConexionBD():
    
    #conexion
    global conexion
    global cursor

    if conexion == None:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="BancoAlcala",
            port=3306
        )

        conexion.autocommit = False
        
        #crear cursor
        cursor = conexion.cursor(buffered=True)
        
        #crear tablas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            dni varchar(255) PRIMARY KEY not null, 
            name varchar(255) not null,  
            password varchar(255) not null
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts(
            accountNumber int PRIMARY KEY not null, 
            dni varchar(255) not null,  
            accountBalance int not null,
            CONSTRAINT pk_accounts FOREIGN KEY(dni) REFERENCES customers(dni) ON DELETE CASCADE
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movements(
            id int PRIMARY KEY not null AUTO_INCREMENT, 
            originAccount int not null,
            destinationAccount int, 
            amount int not null,
            date date not null,
            movementType varchar(255) not null,
            CONSTRAINT pk_movements FOREIGN KEY(originAccount) REFERENCES accounts(accountNumber) ON DELETE CASCADE
        );
        """)


crearConexionBD()

#CUSTOMERS
def listCustomers():
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    return [{"dni": customer[0],"name":customer[1],"password":customer[2]} for customer in customers]

def insertCustomer(dni, name, password):
    cursor.execute(f"INSERT INTO customers VALUES ('{dni}', '{name}', '{password}')")
    conexion.commit()

def deleteCustomer(dni):
    cursor.execute(f"DELETE FROM customers WHERE dni='{dni}'")
    conexion.commit()
    return cursor.rowcount

def findCustomer(dni):
    cursor.execute(f"SELECT * FROM customers WHERE dni='{dni}' LIMIT 1")
    customer = cursor.fetchone()

    if customer: 
        return {"dni": customer[0],"name":customer[1],"password":customer[2]} 
    return None

#ACCOUNTS
def listAccounts(dni):
    cursor.execute(f"SELECT * FROM accounts WHERE dni='{dni}'")
    accounts = cursor.fetchall()
    return [{"accountNumber": account[0],"dni":account[1],"accountBalance":account[2]} for account in accounts]

def newAccounts(accountNumber, dni, accountBalance):
    cursor.execute(f"INSERT INTO accounts VALUES ({accountNumber}, '{dni}', {accountBalance})")
    conexion.commit()

def findAccount(accountNumber):
    cursor.execute(f"SELECT * FROM accounts WHERE accountNumber={accountNumber} LIMIT 1")
    account = cursor.fetchone()

    if account: 
        return {"accountNumber": account[0],"dni":account[1],"accoutBalance":account[2]} 
    return None

def deleteAccount(accountNumber):

    cursor.execute(f"SELECT * FROM accounts WHERE accountNumber={accountNumber}")
    account = cursor.fetchone()
    
    if account: 
        if account[2] == 0:
            cursor.execute(f"DELETE FROM accounts WHERE accountNumber={accountNumber}")
            conexion.commit()
            return {"accountNumber": account[0],"dni":account[1],"accoutBalance":account[2]} 
        if account[2] > 0:
            raise AccountWithBalance("Cuenta con saldo")
    return None
    
#MOVEMENTS
def listMovements(numberAccount):
    cursor.execute(f"SELECT * FROM movements WHERE originAccount={numberAccount} OR destinationAccount={numberAccount}")
    movements = cursor.fetchall()

    return [{"id":movement[0],"originAccount":movement[1],"destinationAccount":movement[2],"amount":movement[3],"date":movement[4],"movementType":movement[5]} for movement in movements]

def newMovements(originAccount, amount,movementType,destinationAccount):
    cursor = conexion.cursor(buffered=True)
    print(destinationAccount)
    try:
        if originAccount == destinationAccount:
            raise AccountnotExits("Cuenta origen igual a cuenta destino")
        if findAccount(originAccount) == None:
            raise AccountnotExits("Cuenta origen no existe")
        
        if movementType == "deposit":
            cursor.execute(f"UPDATE accounts SET accountBalance = accountBalance + {amount} WHERE accountNumber = {originAccount}")
        elif movementType == "withdrawn":
            cursor.execute(f"UPDATE accounts SET accountBalance = accountBalance - {amount} WHERE accountNumber = {originAccount}")
        elif movementType == "transfer":
            if findAccount(destinationAccount) == None:
                raise AccountnotExits("Cuenta destino no existe")
            cursor.execute(f"UPDATE accounts SET accountBalance = accountBalance - {amount} WHERE accountNumber = {originAccount}")
            cursor.execute(f"UPDATE accounts SET accountBalance = accountBalance + {amount} WHERE accountNumber = {destinationAccount}")
        else:
            raise TypeMovementsnotExits("El tipo de movimiento no existe")

        cursor.execute(f"INSERT INTO movements (originAccount,destinationAccount,amount,date,movementType) VALUES ({originAccount}, {destinationAccount}, {amount}, NOW(),'{movementType}')")
        print ("Movimiento realizado")

        conexion.commit()

    except mysql.connector.Error as error :
        print("Error en el movimiento, no se realiza ningún cambio: {}".format(error))
        #deshace los cambios debido a la excepción
        conexion.rollback()
        
    finally:
        cursor.close()
