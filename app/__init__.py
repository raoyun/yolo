# -- coding: utf-8 --
from flask import Flask
from config import Config


yolo = Flask(__name__)
yolo.config.from_object(Config)