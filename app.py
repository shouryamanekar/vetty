from flask import Flask, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import requests
import os

app = Flask(__name__)

BASE_URL = "https://api.coingecko.com/api/v3"
API_KEY = os.getenv('API_KEY')

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": API_KEY
}


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Vetty API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/coins', methods=['GET'])
def list_coins():
    response = requests.get(f"{BASE_URL}/coins/list", headers=headers)
    return jsonify(response.json())


@app.route('/categories', methods=['GET'])
def list_categories():
    response = requests.get(f"{BASE_URL}/coins/categories/list", headers=headers)
    return jsonify(response.json())


@app.route('/coins/<coin_id>', methods=['GET'])
def get_coin(coin_id):
    response = requests.get(f"{BASE_URL}/coins/{coin_id}", headers=headers)
    return jsonify(response.json())


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})


@app.route('/version', methods=['GET'])
def version_info():
    return jsonify({"version": "1.0.0"})


if __name__ == '__main__':
    app.run(debug=True)
