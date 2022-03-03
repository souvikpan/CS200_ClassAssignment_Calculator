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

@app.route("/subtract", methods=["POST"])
def subtract():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    diff = a-b
    response = "Difference of 2 numbers = " + str(diff)
    return response
    
    
@app.route("/find_min", methods=["POST"])
def FIND_MIN():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    if (a > b):
        response = "The minimum of the two number is" + str(b)
    elif (a < b):
        response = "The minimum of the two number is" + str(a)
    else:
        response = "Both the numbers are equal"


if __name__== "__main__":
    app.run()
