from flask import Flask, render_template_string, jsonify
from lco_integration import LCOIntegration
import os

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/api/lco/<site_code>')
def get_lco_data(site_code):
    lco = LCOIntegration(os.getenv('LCO_API_TOKEN'))
    data = lco.get_site_data(site_code)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)