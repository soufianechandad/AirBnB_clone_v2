#!/usr/bin/python3
"""
A ript that starts a Flask web application
your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """Display a welcome message"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
