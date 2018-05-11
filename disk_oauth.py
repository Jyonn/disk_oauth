from flask import Flask, request

from error import Error
from qtb import get_qtb_user_token, update_user_info
from response import error_response, response

app = Flask(__name__)


@app.route('/token', methods=['POST'])
def get_user_token():
    code = request.get_json()['code']
    ret = get_qtb_user_token(code)
    if ret.error is not Error.OK:
        return error_response(ret)
    return response(body=ret.body)


@app.route('/info', methods=['POST'])
def update_info():
    token = request.get_json()['token']
    ret = update_user_info(token)
    if ret.error is not Error.OK:
        return error_response(ret)
    return response(body=ret.body)


if __name__ == '__main__':
    app.run()
