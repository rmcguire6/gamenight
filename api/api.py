from flask import Flask
from flask import render_template

api = Flask(__name__)

rooms=[{'title': 'The Perils of Markenburg','text': 'You stand at the opening of the Fissure of Markenburg. You must choose what you will do.', 'room_id': 0,'choice_one': 'Go to the left', 'choice_two': 'Go forward', 'choice_three': 'Go to the right', 'monsters': None },
{'title': 'A Cavern','text': 'You stand at the opening of a cavern. You must choose what you will do.', 'room_id': 1,'choice_one': 'Go back', 'choice_two': 'Go in', 'choice_three': 'Go to the right', 'monsters':['giant', 'dragon', 'spider', 'troll']},
{'title': 'The Swamp of Markenburg','text': 'You stand at the beginning of the Swamp of Markenburg. You must choose what you will do.', 'room_id': 2,'choice_one': 'Go to the left', 'choice_two': 'Swim forward', 'choice_three': 'Go to the right', 'monsters':['giant carp', 'mermaid', 'giant stinging eel', 'water leeches']},
{'title': 'The Forest of Markenburg','text': 'You stand at the opening of the Forest of Markenburg. You must choose what you will do.', 'room_id': 3,'choice_one': 'Go to the left', 'choice_two': 'Go forward', 'choice_three': 'Go to the right', 'monsters':['giant', 'dragon', 'spider', 'werewolf']},
{'title': 'The Mountain of Markenburg','text': 'You stand at the side of the Mountain of Markenburg. You must choose what you will do.', 'room_id': 4,'choice_one': 'Go to the left', 'choice_two': 'Climb up', 'choice_three': 'Go to the right', 'monsters':['giant', 'dragon','werewolf', 'troll']},
{'title': 'The River of Markenburg','text': 'You stand at the side of the River of Markenburg. You must choose what you will do.', 'room_id': 5,'choice_one': 'Go to the left', 'choice_two': 'Swim forward', 'choice_three': 'Climb the cliff on the right ','monsters':['giant carp', 'mermaid', 'giant stinging eel', 'river nymphs']}]


@api.route("/")
def start_page():
    room=rooms[0]
    game_message='Please start'
    return render_template('page.html', room=room, game_message=game_message)

@api.route("/<int:room_id>")
def build_room(room_id):
    room=rooms[room_id]
    game_message='Please continue'
    return render_template('page.html', room=room, game_message=game_message)

