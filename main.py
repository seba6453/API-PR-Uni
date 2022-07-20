from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
import json
from cargaDBscotiabank import cargaScotiabank

app = Flask(__name__)

CORS(app)


@cross_origin
@app.route('/', methods=['GET'])
def index():
    return "hola"

@cross_origin
@app.route('/File', methods=['POST','OPTIONS'])
def file():
    datos = json.loads(request.data.decode('utf8'))
    confirmacion = cargaScotiabank(rut=datos["Rut"],datos=datos["InfText"],nroCuenta=datos["nroCuenta"])
    return {"respuesta":confirmacion}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
