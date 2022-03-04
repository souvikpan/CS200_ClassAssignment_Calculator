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
    response = "sum of 2 numbers = " + str(sum)
    return response




if __name__== "__main__":
    app.run()
