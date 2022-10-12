from flask import Flask, request, request, Response, jsonify

from engine import *
from werkzeug.utils import secure_filename
from pathlib import Path

# Initialize flask app and session key
app = Flask(__name__)


# Health check route
@app.route("/isalive")
def is_alive():
    print("/isalive request")
    status_code = Response(status=200)
    return status_code
 

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    print("/predict request")
    req_json = request.get_json()
    json_instances = req_json["instances"]

    Instance_list = [str(j) for j in json_instances]
    
    # Call process text
    ner_results= process_text(Instance_list)

    return jsonify({
        "predictions": str(ner_results)
    })

