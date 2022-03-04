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
    
@app.route("/expo", methods=["POST"])
def expo(): 
	jsonStr = request.get_json()
	jsonObj = json.loads(jsonStr)
	a=int(jsonObj['N1'])
	b=int(jsonObj['N2'])
	return str(a) + " raised to the power " + str(b)+ "is equal to "+ str(a**b)  

@app.route("/bitwiseXor", methods=["POST"])
def bitwiseXor():     
	jsonStr = request.get_json()
	jsonObj = json.loads(jsonStr)
	a=int(jsonObj['N1'])
	b=int(jsonObj['N2'])
	xor=a^b
	response = "Bitwise Xor of 2 numbers = " + str(xor)
	return response

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



@app.route("/bitAND", methods=["POST"])
def bitAND(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    num=a&b
    response = "And operator of 2 numbers is " + str(num)
    return response

#code added by group tech warriors
@app.route("/multiply", methods=["POST"])
def multiply(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    mul=a*b
    response = f"multiplication of {a} and {b} = {mul}"
    return response

@app.route("/LOGICAL_AND", methods=["POST"])
def LOGICAL_AND(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    LOGIC_AND = a and b
    response = "logical and of a and b is = " + str(LOGIC_AND)

    return response

if __name__== "__main__":
    app.run()
