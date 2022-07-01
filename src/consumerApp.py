from email import message
import re
import requests
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

@app.route("/", methods=["GET"])
def consumer():
     response = "OOPS ! Service not working"
     try:
        response = requests.get(url="http://flask-service:5000")
        print(response.content)
        message = list(json.loads(response.content.decode('utf-8')).values())[1]
     except:
         return("Cannot connect to backend. API not working")
     print(message)
     return reverse(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)