from flask import Flask
from flask import render_template

api = Flask(__name__)

@api.route("/")
def start_page():
    page={'title': 'The Fissure of Markenburg', 'text':'You must choose what you will do.', 'choice_one': 'Go to the left', 'choice_two': 'Go forward', 'choice_three': 'Go to the right'}
    return render_template('page.html', page=page)
