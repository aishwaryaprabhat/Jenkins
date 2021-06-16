import pickle
from flask import Flask, request, jsonify
from flasgger import Swagger
import numpy as np
import os 


app = Flask(__name__)
swagger = Swagger(app)

port = int(os.environ.get("PORT", 5000))

@app.route('/')
def landing_page():

  return "Hello, world!", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)