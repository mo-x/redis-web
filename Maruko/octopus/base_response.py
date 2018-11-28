from typing import Any


class BaseResponse:
    code = None
    msg = ""
    result = None

    def __init__(self, code, msg, result):
        self.code = code
        self.msg = msg
        self.result = result

    def __init__(self):
        self.code = 100

    def get_code(self):
        return self.code

    def get_msg(self):
        return self.msg

    def get_result(self):
        return self.result

    # @staticmethod
    # def success(self):
    #     self.code = 100
    #     self.msg = "success"
    #     self.result = "success"
    @staticmethod
    def success(x):
        t = BaseResponse()
        t.code = 100
        t.msg = "success"
        t.result = x
        return t


r = BaseResponse()
r = BaseResponse.success(False)
print(r)
