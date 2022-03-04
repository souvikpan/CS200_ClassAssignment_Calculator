import json
from flask import Flask, render_template, request, jsonify 
import math  

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
    

@app.route("/bitwiseXor", methods=["POST"])
def bitwiseXor(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    
    # Logic for function assigned to you as in pdf
    xor=a^b
    response = "Bitwise Xor of 2 numbers = " + str(xor)
    return response


@app.route("/bitAND", methods=["POST"])
def bitAND(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    num=a&b
    response = "And operator of 2 numbers is " + str(num)
    return response

@app.route("/logarithm", methods=["POST"])
def logarithm(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    log=math.log(a,b)
    response="Log of Number-1 is calculated with  Number-2 as the base "+str(log)
    return response

if __name__== "__main__":
    app.run()
