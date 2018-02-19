from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    """Devuelve estado"""
    return jsonify({ 'status': 'OK'})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
