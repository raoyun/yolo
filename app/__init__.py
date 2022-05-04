# -- coding: utf-8 --
from flask import Flask
from config import Config
from flask_cors import CORS

yolo = Flask(__name__)
CORS(yolo, supports_credentials=True)

yolo.config.from_object(Config)