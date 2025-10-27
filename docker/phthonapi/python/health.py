from flask import Flask, jsonify
import logging
import sys

app = Flask(__name__)

# Configure logging to stdout
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

@app.route('/api/health')
def health():
    app.logger.info("Health endpoint called")
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)