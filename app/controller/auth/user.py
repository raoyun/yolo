# -- coding: utf-8 --
from flask import Blueprint
from flask import jsonify
from app.dao.auth.UserDao import UserDao
from flask import request
auth = Blueprint("auth", __name__, url_prefix="/auth")


# 这里以auth.route注册的函数都会自带/auth，所以url是/auth/register
@auth.route("/register", methods=['POST'])
def register():
    data = request.get_json(force=True)
    username, password = data.get('username'), data.get('password')
    if not username or not password:
        return jsonify(dict(code=101, msg='用户名或密码不能为空'))
    email, name = data.get('email'), data.get('name')
    if not email or not name:
        return jsonify(dict(code=101, msg='邮件和姓名不能为空'))
    err = UserDao.register_user(username,name,password,email)
    if err is not None:
        return jsonify(dict(code=110, msg=err))
    return jsonify(dict(code=0, msg='注册成功'))