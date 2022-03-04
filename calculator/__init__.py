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
@app.route("/Bitwise_NOR", methods=["POST"])
def Bitwise_NOR():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    Bitwise_NOR=~(a|b)
    response = "The Bitwise NOR of these two numbers is :  " + str(Bitwise_NOR)
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

if __name__== "__main__":
    app.run()
