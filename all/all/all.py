from flask import Flask, request, redirect, jsonify
import requests

app = Flask(__name__)

@app.route("/all", methods=['GET'])
def query():

    r = requests.get('https://corona.lmao.ninja/v2/all')

    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3001)

    
