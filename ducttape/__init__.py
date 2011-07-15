from flask import *
from datetime import *
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ducttape-site.db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'lolverysecret'
db = SQLAlchemy(app)
Markdown(app, safe_mode="escape")

import ducttape.filters
import ducttape.views
import ducttape.models

@app.context_processor
def inject_time():
    return dict(current_datetime = datetime.utcnow())
