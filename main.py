import ast

src = """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
"""

print(ast.dump(ast.parse(src), indent=4))