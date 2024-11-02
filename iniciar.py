from flask import Flask
import subprocess
import os
import signal

app = Flask(__name__)

process = None  # Variable global para almacenar el proceso

@app.route('/start-server', methods=['POST'])
def start_server():
    global process
    if process is None:  # Asegúrate de que no haya un proceso en ejecución
        process = subprocess.Popen(['python', r'C:\Users\frane\OneDrive\Escritorio\ServerPibes\iniciar.py'])  # Cambia la ruta según tu configuración
        return 'Server started!', 200
    else:
        return 'Server is already running!', 400

@app.route('/stop-server', methods=['POST'])
def stop_server():
    global process
    if process is not None:
        os.kill(process.pid, signal.SIGTERM)  # Enviar señal para terminar el proceso
        process = None  # Reinicia la variable del proceso
        return 'Server stopped!', 200
    else:
        return 'No server is running!', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
