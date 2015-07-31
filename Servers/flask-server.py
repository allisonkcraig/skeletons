import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show our index page."""

    return render_template("index.html")


@app.route('/page1')
def fortune():
    """Render page 1"""
    
    return render_template("page1.html")


@app.route('/page2')
def weather():
    """Render page 2"""

    return render_template("page2.html")


if __name__ == "__main__":
    app.run(debug=True)