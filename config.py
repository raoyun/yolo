# -- coding: utf-8 --
# 基础配置类
import os


class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'yolo.log')

    # Flask jsonify编码问题
    JSON_AS_ASCII = False