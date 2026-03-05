from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Importante para que el navegador no bloquee la petición desde el frontend

contador_total = 0

@app.route('/actualizar', methods=['POST'])
def actualizar():
    global contador_total
    datos = request.json
    valor = datos.get('valor', 0)
    contador_total += valor
    print(f"Contador actualizado: {contador_total}")
    return jsonify({"status": "ok", "nuevo_total": contador_total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)