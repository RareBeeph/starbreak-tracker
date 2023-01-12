from flask import Flask
from .controllers import blueprints

app = Flask(__name__)
[app.register_blueprint(bp) for bp in blueprints]


@app.route("/")
def hello_world() -> str:
    return "<p>Hello, world!</p>"
