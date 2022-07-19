from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
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
    confirmacion = cargaScotiabank(rut=request.data[1].decode('utf8'),datos=request.data[0].decode('utf8'),nroCuenta=111)
    return {"respuesta":confirmacion}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
