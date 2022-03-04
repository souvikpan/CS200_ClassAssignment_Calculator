import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/add", methods=["POST"])
def ADD(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    sum=a+b
    response = "sum of 2 numbers = " + str(sum)
    return response
    
@app.route("/xyz", methods=["POST"])
def XYZ(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    
    # Logic for function assigned to you as in pdf
    
    return 1

@app.route("/isequal", methods=["POST"])
def isequal():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])

    if (a==b):
        return "The numbers are equal"
    else:
        return "The numbers are NOT equal"


if __name__== "__main__":
    app.run()
