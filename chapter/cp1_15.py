from flask import Flask, jsonify, request
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Planetary API'), 200


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f'Sorry {name}, you are not old enough'), 401
    return jsonify(message=f'Welcome {name}, you are old enough'), 200


@app.route('/url_variables/<string:name>/<int:age>')
def url_variable(name: str, age: int):
    if age < 18:
        return jsonify(message=f'Sorry {name}, you are not old enough'), 401
    return jsonify(message=f'Welcome {name}, you are old enough'), 200


if __name__ == '__main__':
    app.run()
