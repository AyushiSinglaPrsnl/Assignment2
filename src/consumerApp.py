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
     response = requests.get(url="http://127.0.0.1:5000/")
     print(response.content)
     message = list(json.loads(response.content.decode('utf-8')).values())[1]
     
     print(message)
     return reverse(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)