import flask
import random
import string
import os
import flask_sqlalchemy
import flask_migrate

basedir = os.path.abspath(os.path.dirname(__file__)) # Try to avoid hardcoding paths, use os

app = flask.Flask(__name__) # Remember: __name__ is the name of the file where the code is written

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'ecole.db')
app.config['SECRET_KEY'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=256))

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


from app import routes,error_handlers, models