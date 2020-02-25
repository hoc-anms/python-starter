from flask import Flask

app = Flask(__name__)

@app.route( "/" )

def index():
    return "Hello, World!"

# with a specific name
# @app.route( "/david" )
# def david():
#     return "Hello, David!"
#
# @app.route( "/maria" )
# def maria():
#     return "Hello, Maria!"

# with variable names
@app.route( "/<string:name>" )

def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"
