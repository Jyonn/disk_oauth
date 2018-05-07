""" 180226 Adel Liu

错误表，在编码时不断添加
自动生成eid
"""


class E:
    _error_id = 0

    def __init__(self, msg, release_e=None):
        self.eid = E._error_id
        self.msg = msg
        self.release = release_e if isinstance(release_e, E) else None
        E._error_id += 1


class Error:
    # Debug 错误
    OK = E("没有错误")

    # Release 错误
    ERROR_PARAM = E("参数错误")
    SYSTEM_ERROR = E("系统错误")
    REQUIRE_UNAVAILABLE = E("请求错误")

    STRANGE = E("未知错误")
    QTB_AUTH_FAIL = E("齐天簿身份认证失败")
    QTB_GET_INFO_FAIL = E("齐天簿获取用户信息失败")

    @classmethod
    def get_error_dict(cls):
        error_dict = dict()
        for k in cls.__dict__:
            if k[0] != '_':
                e = getattr(cls, k)
                if isinstance(e, E):
                    error_dict[k] = dict(eid=e.eid, msg=e.msg)
        return error_dict
