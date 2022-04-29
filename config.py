# -- coding: utf-8 --
# 基础配置类
import os


class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'yolo.log')

    # Flask jsonify编码问题
    JSON_AS_ASCII = False

    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "123456"
    DBNAME = 'yolo'

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False