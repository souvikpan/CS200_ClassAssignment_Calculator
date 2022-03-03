import json
from flask import Flask, render_template, request, jsonify   
from math import lcm

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
    response =   str(sum)
    return response
    
@app.route("/nth_root", methods=["POST"])
def nth_root (): 
    jsonStr  = request.get_json()
    jsonObj  = json.loads(jsonStr)
    a1= int(jsonObj['N1'])
    b1= int(jsonObj['N2'])
    outpt=((a1)**(1/b1))
    response  = str(outpt)
    return  response
    # Logic for function assigned to you as in pdf
    
    

    
@app.route("/lcm", methods=["POST"])
def subtract(a,b):
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    return lcm(a,b)
    

if __name__== "__main__":
    app.run()
