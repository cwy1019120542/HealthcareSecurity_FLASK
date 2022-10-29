from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_extention(app):
    db.init_app(app)