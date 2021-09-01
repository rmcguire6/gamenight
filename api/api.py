from flask import Flask
from flask import render_template

api = Flask(__name__)

rooms=[{'title': 'The Perils of Markenburg','text': 'You stand at the opening of the Fissure of Markenburg. You must choose what you will do.', 'room_id': 0,'left': 3, 'forward': 5, 'right': 1, 'monsters': None },
{'title': 'A Cavern','text': 'You stand in a  cavern. You must choose what you will do.', 'room_id': 1,'left': 5, 'forward': 4, 'right': 1, 'monsters':['giant', 'dragon', 'spider', 'troll']},
{'title': 'The Swamp of Markenburg','text': 'You stand at the swamp of Markenburg. You must choose what you will do.', 'room_id': 2,'left': 1, 'forward': 2, 'right': 4, 'monsters':['giant carp', 'mermaid', 'giant stinging eel', 'water leeches']},
{'title': 'The Forest of Markenburg','text': 'You stand in the forest of Markenburg. You must choose what you will do.', 'room_id': 3,'left': 4, 'forward': 3, 'right': 5, 'monsters':['giant', 'dragon', 'spider', 'werewolf']},
{'title': 'The Mountain of Markenburg','text': 'You stand  in the mountains of Markenburg. You must choose what you will do.', 'room_id': 4,'left': 5, 'forward': 2, 'right': 4, 'monsters':['giant', 'dragon','werewolf', 'troll']},
{'title': 'The River of Markenburg','text': 'You stand at the river of Markenburg. You must choose what you will do.', 'room_id': 5,'left': 3, 'forward': 2, 'right':  1,'monsters':['giant carp', 'mermaid', 'giant stinging eel', 'river nymphs']}]


@api.route("/")
def start_page():
    room=rooms[0]
    game_message='Please start'
    return render_template('page.html', room=room, game_message=game_message)

@api.route("/room/<int:room_id>")
def build_room(room_id):
    room=rooms[room_id]
    game_message='Please continue'
    return render_template('page.html', room=room, game_message=game_message)

