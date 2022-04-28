# -- coding: utf-8 --
from app import yolo
from app.utils.log import Log


@yolo.route('/')
def hello_world():
    log = Log("hello world专用")
    log.info("有人访问你的网站了")
    return 'Hello World!'


if __name__ == "__main__":
    yolo.run("0.0.0.0", threaded=True, port="7777")
