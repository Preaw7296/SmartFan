from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask with Gunicorn!"})

@app.route('/status')
def status():
    return jsonify({"status": "Running", "service": "Flask API"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
Flask
gunicorn
