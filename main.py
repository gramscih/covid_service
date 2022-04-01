from flask import Flask, jsonify
import json
import os

DATA_PATH = "src/%s.json"
HOSPITAL_NAMES = ["hells_pass_hospital", "univalle"]
app = Flask(__name__)


@app.get("/hospitals")
def get_hospitals_name():
    files = os.listdir("src/")
    files_name = [file.split('.')[0] for file in files]
    print(files_name)
    return jsonify(files_name), 200


@app.get("/hospitals/<hospital_name>")
def get_hospital_data(hospital_name):
    file_path = DATA_PATH % hospital_name
    with open(file_path) as hells_data:
        data = json.load(hells_data)
        return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True, port=80)
