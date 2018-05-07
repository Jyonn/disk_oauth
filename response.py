""" Adel Liu 180111

函数返回、方法返回、错误返回类
"""

from flask import jsonify

from common import DEBUG, deprint
from error import Error, E


class Method:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    OPTIONS = 'OPTIONS'


class Ret:
    """
    函数返回类
    """
    def __init__(self, error=Error.OK, body=None, append_msg=''):
        if not isinstance(error, E):
            body = error
            error = Error.OK
        self.error = error
        self.body = body or []
        self.append_msg = append_msg


def response(e=Error.OK, msg=Error.OK.msg, body=None):
    """
    回复HTTP请求
    """
    resp = {
        "status": 'debug' if DEBUG else 'release',
        "code": e.eid,
        "msg": msg,
        "body": body or [],
    }

    return jsonify(resp)


def error_response(e, append_msg=""):
    """
    回复一个错误
    171216 当error_id为Ret类时，自动转换
    """
    if isinstance(e, Ret):
        append_msg = e.append_msg
        e = e.error
    if not isinstance(e, E):
        deprint(str(e))
        return error_response(Error.STRANGE, append_msg='error_response error_id not E')

    if not DEBUG and e.release:
        e = e.release
    return response(e=e, msg=e.msg + append_msg)
