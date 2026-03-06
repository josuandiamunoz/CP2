from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

COUNTER_FILE = "/data/contador.txt"

def leer_contador():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0

def guardar_contador(valor):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(valor))

# Inicializamos el contador
contador_total = leer_contador()

@app.route('/api/actualizar', methods=['POST'])
def actualizar():
    global contador_total
    datos = request.json
    valor = datos.get('valor', 0)
    contador_total += valor
    guardar_contador(contador_total)
    print(f"Contador actualizado: {contador_total}")
    return jsonify({"status": "ok", "nuevo_total": contador_total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)