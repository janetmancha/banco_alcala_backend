from flask import Flask, request, jsonify
from app.routes.common import app
from app.persistencia.MySQL import crearConexionBD

app.run(debug=True, host="0.0.0.0")
