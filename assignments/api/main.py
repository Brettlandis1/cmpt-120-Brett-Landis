# The Flask package we need in order to run our REST APIs
from flask import Flask, jsonify

# Creating a new "app" by using the Flask object constructor method.
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


# Checks to see of then
if __name__ == "__main__":
    # Runs the Flask application only if this file itself being run.
    app.run()
