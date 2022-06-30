from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/json', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "id" : "1",
            "message" : "Hello World",
        }
        print(data)
        return jsonify(data)
  
if __name__=='__main__':
    app.run(host ='0.0.0.0', port = 5000,debug=True)