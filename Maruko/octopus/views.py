import json

from django.http import HttpResponse

from .RedisUtil import RedisUtil

from .base_response import BaseResponse


# 获取redis key列表
def keys(request):
    key_list = RedisUtil.get_conn().keys()
    print(len(key_list))
    result_list = []
    for key in key_list:
        value = {"key": key, "type": RedisUtil.get_conn().type(key)}
        result_list.append(value)
    return HttpResponse(json.dumps(result_list), content_type="application/json")


def db_size(request):
    return HttpResponse(RedisUtil.get_conn().dbsize(), content_type="application/json")


def get_value(request, key):
    return HttpResponse(RedisUtil.get_conn().get(key), content_type="application/json")


def set_value(request, key, value):
    print(key, value)
    RedisUtil.get_conn().type(key)
    r = BaseResponse.success(RedisUtil.get_conn().set(key, value))
    return HttpResponse(json.dumps(r.__dict__), content_type="application/json")


def value_clear(request, key):
    is_exist = RedisUtil.get_conn().exists(key)
    if is_exist:
        value_type = RedisUtil.get_conn().type(key)
        if value_type == "string":
            RedisUtil.get_conn().set(key, "")
    return None
