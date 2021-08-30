from flask import Flask 
from flask import render_template

api = Flask(__name__)

@api.route("/")
def start_page():
    return render_template('layout.html')