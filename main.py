from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
from cargaDBscotiabank import cargaScotiabank

app = Flask(__name__)

CORS(app)


@cross_origin
@app.route('/File', methods=['POST','OPTIONS'])
def file():
    confirmacion = cargaScotiabank(rut='20168189-8',datos=request.data.decode('utf8'),nroCuenta=111)
    return {"respuesta":confirmacion}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
