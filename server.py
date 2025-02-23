"""A simple Flask web server that responds with a greeting."""
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    """Handle GET requests to root URL by returning a greeting."""
    return "Hello there!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
