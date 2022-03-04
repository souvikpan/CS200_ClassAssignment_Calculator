import json
from flask import Flask, render_template, request, jsonify   
app = Flask(__name__)
import math 
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
@app.route("/exponentiation", methods=["POST"])
def exp(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    x=int(jsonObj['N1'])
    y=int(jsonObj['N2'])
    value=pow(x,y)
    response = str(x) +" power " + str(y) + " is " + str(value)
    return response
    # Logic for function assigned to you as in pdf



if __name__== "__main__":
    app.run()
