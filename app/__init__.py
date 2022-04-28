# -- coding: utf-8 --
from flask import Flask
from config import Config
from app.controller.auth.user import auth

yolo = Flask(__name__)
yolo.config.from_object(Config)

# 注册蓝图
yolo.register_blueprint(auth)

yolo.config.from_object(Config)