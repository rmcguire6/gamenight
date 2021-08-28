from flask import Flask 

api = Flask(__name__)

@api.route("/")
def hello_to_gamenight():
    return"<p>Hello to Chingu gamenight</p>"