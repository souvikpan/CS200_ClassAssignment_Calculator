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
    response =   str(sum)
    return response
    
@app.route("/nth_root", methods=["POST"])
def nth_root (): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    outpt=((a)**(1/b))
    response = str(outpt)
    return response
    # Logic for function assigned to you as in pdf
    
    

@app.route("/subtract", methods=["POST"])
def subtract():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    return a-b
    
    
    

if __name__== "__main__":
    app.run()
