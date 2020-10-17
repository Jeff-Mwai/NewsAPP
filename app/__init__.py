from flask import Flask
from .config import DevConfig

#Command to initialize the application
app = Flask(__name__, instance_relative_config = True)

#instance to config the application
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views