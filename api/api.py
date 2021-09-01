from flask import Flask
from flask import render_template

api = Flask(__name__)

@api.route("/")
def start_page():
    room={'title': 'The Perils of Markenburg','text': 'You stand at the opening of the Fissure of Markenburg. You must choose what you will do.', 'room_id': 0,'choice_one': 'Go to the left', 'choice_two': 'Go forward', 'choice_three': 'Go to the right'}
    return render_template('page.html', room=room)
