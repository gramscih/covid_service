from flask import Flask

app = Flask(__name__)

hells_hospital_data = {
    "date": ""
}


@app.get("/hellsPassHospital")
def get_hells_pass_hospital_data():
    pass


app.run(debug=True)
