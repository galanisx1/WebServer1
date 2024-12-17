from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')  # Define la carpeta de archivos estáticos
CORS(app)

# Ruta para servir el archivo index.html
@app.route('/')
def serve_index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

# Ruta API para procesar datos
@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.json  # Obtiene los datos en formato JSON
    if not data:
        return jsonify({'error': 'No data received'}), 400

    user_input = data.get('input', '')
    result = f"Hola, procesaste: {user_input}"
    return jsonify({'result': result})  # Devuelve la respuesta en JSON

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Puerto para Render
    app.run(host='0.0.0.0', port=port)

