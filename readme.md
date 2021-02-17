DESCRIPCION BANCO ALCALA:
Backend Banco de Alcala: en este programa, se podrá dar de alta y baja de clientes y de cuentas bancarias, así como realizar los siguientes movimientos bancarios: ingresar dinero, sacar dinero y trasnferencias

REPOSITORIO:
https://github.com/janetmancha/banco_alcala_backend.git

REQUISITOS:
- instalar mysql : brew install mysql
- Crear la base de datos antes de ejecutar el programa:
    - arrancar mysql: brew services start mysql
    - conectar con sql: mysql -uroot
    - CREATE DATABASE IF NOT EXISTS BancoAlcala character set utf8;
    - ver las bases de datos para comprobar que se haya creado: show databases;
- instalar mysql.conector: pip install mysql-connector-python

RUN:
- Ejecutar programa: python3 main.py en la carpeta donde está el programa

EXAMPLES:
---clientes---
- listar clientes: curl localhost:5000/api/customers
- Insertar nuevo cliente: curl -d '{"dni": "1234P","name": "pili", "password": "pass3"}' -H "content-type: application/json" localhost:5000/api/customers
- Buscar un cliente en concreto, en este caso buscar a cliente pili: curl localhost:5000/api/customers/1234P
- Borrar Cliente: curl -X DELETE localhost:5000/api/customers/1234P

---cuentas---
- listar cuentas de un cliente: curl "localhost:5000/api/accounts?filterByDNI=1234P"
- Insertar nueva cuenta: curl -d '{"accountNumber": 3,"dni": "1234P", "accountBalance": 700}' -H "content-type: application/json" localhost:5000/api/accounts
curl -d '{"accountNumber": 4,"dni": "1234P", "accountBalance": 0}' -H "content-type: application/json" localhost:5000/api/accounts
Buscar un cuenta en concreto: curl localhost:5000/api/accounts/3
- Borrar Cliente: curl -X DELETE localhost:5000/api/accounts/3
curl -X DELETE localhost:5000/api/accounts/4
curl -X DELETE localhost:5000/api/accounts/200

---movimientos---
- listar movimientos de una cuenta: curl localhost:5000/api/movements/4
- Insertar nuevo movimiento: curl -d '{"accountNumber": 3,"dni": "1234P", "accountBalance": 700}' -H "content-type: application/json" localhost:5000/api/accounts
curl -d '{"originAccount": 4,"amount": 1245, "movementType": "deposit","destinationAccount":2}' -H "content-type: application/json" localhost:5000/api/movements
- Sacar dinero: curl -d '{"originAccount": 4,"amount": 400, "movementType": "withdrawn"}' -H "content-type: application/json" localhost:5000/api/movements
- Trasferir dinero: curl -d '{"originAccount": 4,"amount": 100, "movementType": "transfer", "destinationAccount": 3}' -H "content-type: application/json" localhost:5000/api/movements

SWAGGER: 
- Ejecutar: boton derecho sobre el fichero banco_alcala.yaml/Preview Swagger

TEST:
- Ejecutar todos los test: python3 -m unittest -v

TIPS:
- MySQL: 
    arrancar mysql: brew services start mysql
    para conectar: mysql -uroot
    usuario: root, sin contraseña
    MySQLWorkbench  herramienta visual de bases de datos MySQL

+++++++++++++++ ROADMAP+++++++++++++++
- Inicio sesión 
- Cerrar sesión 
- Crear los Endopints:
    Movimientos: 
        Hacer Transferencia, sacar dinero o ingresar dinero

- Crear los test:
    Movimientos: 
        Hacer Transferencia, sacar dinero o ingresar dinero

+++++++++++++++ CHANGELOG: +++++++++++++++
- SWAGGER: definidos los siguiente Endpoints:
    Crear Cliente
    Borrar Cliente
    Listar Clientes:
    Crear Cuenta
    Borrar Cuenta
    Listar Cuentas
    Hacer Transferencia
    Sacar Dinero
    Meter Dinero
    Listar Movimientos
    Listar un movimiento
- Crear base de datos MySQL (sin la tablas)
- Crear las tablas de la base de datos:
    Tabla Clientes: dni, nombre, contraseña
    Tabla Cuentas: numero de cuenta, saldo cuenta, dni
    Tabla Movimientos:  id, cuenta origen, cuenta destino numero de cuenta destino, importe, fecha movimiento, tipo de movimiento(1.ingreso, 2.sacar dinero, 3.transferencia)
- Crear los Endopints:
    Clientes:
        Listar todos los Clientes
        Crear Cliente
        Buscar Cliente
        Borrar Cliente
    Cuentas:
        Listar todas cuentas de un cliente
        Crear Cuenta
        Buscar Cuenta por numero de cuenta
        Borrar Cuenta
    Movimientos:
        Listar movimientos de una cuenta
- Crear los test:
    Clientes:
        Listar todos los Clientes
        Crear Cliente
        Buscar Cliente
        Borrar Cliente
    Cuentas:
        Crear Cuenta
        Listar cuentas de un cliente
        Buscar Cuenta por numero de cuenta
        Borrar Cuenta
    Movimientos:
        Listar movimientos de una cuenta