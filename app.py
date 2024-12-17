from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para solicitudes desde el frontend

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.json  # Obtiene los datos en formato JSON
    if not data:
        return jsonify({'error': 'No data received'}), 400

    user_input = data.get('input', '')
    result = f"Hola, procesaste: {user_input}"
    return jsonify({'result': result})  # Devuelve la respuesta en JSON

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render asigna un puerto dinámico
    app.run(host='0.0.0.0', port=port)
