import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use: /USERNAME/MESSAGE"

# if we type /Paraic into the url then the message "Hi Paraic" is returned on screen
@app.route("/<username>")
def user(username):
    return "Hi " + username

# if we type /Paraic/thisMessage into the url then "Paraic: thisMessage" is returned on screen
@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)