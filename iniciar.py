from flask import Flask
import os

app = Flask(__name__)

@app.route('/start-server', methods=['POST'])
def start_server():
    os.system(r'start C:\Users\frane\OneDrive\Escritorio\ServerPibes\init.bat')  # Cambia la ruta según tu configuración
    return 'Server started!', 200

@app.route('/stop-server', methods=['POST'])
def stop_server():
    os.system('taskkill /F /IM java.exe')  # Esto matará el proceso de Java, asegúrate de que sea seguro
    return 'Server stopped!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

