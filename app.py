# app.py
from flask import Flask, render_template, request, jsonify
from converter import convert_to_sinhala
import webview
import threading
import time
import sys, os
import socket
import atexit
import signal

def resource_path(relative_path):
    """ Get absolute path for PyInstaller or running from source """
    try:
        # PyInstaller stores data in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    addr, port = s.getsockname()
    s.close()
    return port

app = Flask(
    __name__,
    template_folder=resource_path("templates"),
    static_folder=resource_path("static")
)

@app.route('/')
def index():
    return render_template('preloader.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    singlish_text = data.get('text', '')
    sinhala_text = convert_to_sinhala(singlish_text)
    return jsonify({'result': sinhala_text})

def start_flask(port):
    # Turn off the reloader and debug in packaged app
    app.run(host='127.0.0.1', port=port, debug=False, use_reloader=False, threaded=True)

def shutdown_server():
    # Called on exit to try to cleanup
    try:
        func = request.environ.get('werkzeug.server.shutdown')
        if func:
            func()
    except Exception:
        pass

def on_exit(signum=None, frame=None):
    # Called on ctrl-c or termination
    try:
        webview.destroy_window()
    except Exception:
        pass
    sys.exit(0)

if __name__ == '__main__':
    atexit.register(on_exit)
    signal.signal(signal.SIGINT, on_exit)
    signal.signal(signal.SIGTERM, on_exit)

    port = int(os.environ.get("ODS_PORT", find_free_port()))
    flask_thread = threading.Thread(target=start_flask, args=(port,), daemon=True)
    flask_thread.start()

    # give flask a moment to start
    time.sleep(0.8)

    url = f"http://127.0.0.1:{port}/"
    try:
        # create window
        webview.create_window(
            title="ODSD Singlish Converter",
            url=url,
            width=1100,
            height=700,
            resizable=True,
            confirm_close=True,
        )
        # Start GUI loop (blocks)
        webview.start()
    except Exception as e:
        print("Failed to start webview GUI:", e)
        print("Open the app in your browser at:", url)

