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
    
@app.route("/MOD", methods=["POST"])
def MOD(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    MOD=a%b
    response = "modulus of 2 numbers = " + str(MOD)
    return response


    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])

    log=math.log(a,b)
    response="Log of Number-1 is calculated with  Number-2 as the base "+str(log)
    return response
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
       
@app.route("/shiftdeciright", methods=["POST"])
def shiftdeciright(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=float(jsonObj['N1'])
    b=float(jsonObj['N2'])
    shift =a*10
    shift2 =b*10
    response ="Shfifting decimal right " + str(shift) +" and "+ str(shift2)
    return response
    

@app.route("/lor", methods=["POST"])
def lor(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a=jsonObj['N1']
    b=jsonObj['N2']
    num=a or b
    response = "Logical or of 2 numbers is " + str(num)
    return response
    
@app.route("/rightshift", methods=["POST"])
def RIGHTSHIFT(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
>>>>>>> 9e08e9d... solved an error of other
    
    return 1




if __name__== "__main__":
    app.run()
