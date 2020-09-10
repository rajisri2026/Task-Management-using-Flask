from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug = True)
