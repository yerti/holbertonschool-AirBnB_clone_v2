#!/usr/bin/python3
"""  script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """Delete current session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Render a HTML page with a list of all State objects sorted by name"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
