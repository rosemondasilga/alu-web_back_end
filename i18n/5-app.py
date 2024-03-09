#!/usr/bin/env python3

"""
This is a basic Flask application with
internationalization support using Flask-Babel.
"""


from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Retrieve user from the mocked user table by user ID.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Set the current user to flask.g.user if user
    ID is passed via login_as parameter.
    """
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@app.route('/')
def index():
    """
    Render the index template and display
    appropriate welcome message based on login status.
    """
    if g.user:
        welcome_msg = gettext("You are logged in as %(username)s.")\
            % {'username': g.user['name']}
    else:
        welcome_msg = gettext("You are not logged in.")
    return render_template('5-index.html', welcome_msg=welcome_msg)


if __name__ == '__main__':
    app.run(debug=True)


# def gettext(message):
#     """
#     Translate a message to the current language.

#     This function is used to translate
#     messages to the appropriate language based on the current locale.

#     """
#     # Actual implementation of translation logic goes here
#     pass
