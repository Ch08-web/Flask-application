import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

AUTOGROQ_API_URL = os.environ.get('AUTOGROQ_API_URL')
AUTOGROQ_API_KEY = os.environ.get('AUTOGROQ_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query_autogroq():
    user_input = request.json.get('input')
    headers = {'Authorization': f'Bearer {AUTOGROQ_API_KEY}'}
    response = requests.post(AUTOGROQ_API_URL, json={'query': user_input}, headers=headers)
    result = response.json()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
