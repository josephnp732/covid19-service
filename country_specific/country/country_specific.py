from flask import Flask, request, redirect, jsonify
import requests

app = Flask(__name__)

@app.route("/countries/<country>", methods=['GET'])
def query(country):

    url = 'https://corona.lmao.ninja/v2/countries/' + country
    r = requests.get(url)

    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3003)

    
