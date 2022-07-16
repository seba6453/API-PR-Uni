from flask import Flask, request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)

CORS(app)

# GET, POST, PUT, DELETE
@app.route('/<usuario>',methods=['GET'])
def indexGet(usuario):
    return 'hola ' + usuario

@app.route('/<usuario>',methods=['POST'])
def indexPost(usuario):
    return 'hola '

@cross_origin
@app.route('/File', methods=['POST','OPTIONS'])
def file():
    print(request.data)
    return {"respuesta":"Archivo cargado"}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
