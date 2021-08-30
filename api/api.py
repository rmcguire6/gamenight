from flask import Flask 
from flask import render_template

api = Flask(__name__)

@api.route("/")
def start_page():
    page={'pagetitle': 'the entrance to the dungeons of Markenburg', 'pagetext':'You must choose what you will do.', 'choice_one': 'Stay here', 'choice_two': 'Go forward'}
    return render_template('startpage.html', page=page)