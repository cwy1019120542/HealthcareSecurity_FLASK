from flask import Flask
from config import Config
from extension import init_extention, db
from response import error_list
from route import route_dict
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
init_extention(app)
Migrate(app, db)
for error in error_list:
    app.register_error_handler(*error)
for view, url in route_dict.items():
    app.add_url_rule(url, view_func=view.as_view(view.__name__))