import numpy as np
from flask import Flask ,render_template,request,jsonify,url_for
import pickle

app = Flask(__name__)

model=pickle.load(open("model.pkl","rb"))
@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict",methods=["POST"])
def predict():
    age = int(request.form['age'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    sex = int(request.form['sex'])
    smoker = int(request.form['smoker'])
    region = int(request.form['region'])
    features = np.array([age, bmi, children, sex, smoker, region])
    features = features.reshape(1, -1)
    prediction = model.predict(features)[0]
    return render_template("prediction.html", prediction_text=f"Your predicted insurance price is :  $ {prediction:,.2f}")

if __name__=="__main__":
    app.run(debug=True)
