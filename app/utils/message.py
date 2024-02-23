import os

def success_msg(msg):
    """

    :param msg: 如果传入的是字符串，则正常返回json;如果是字典类型，则返回字典数据+消息模板
    :return:
    """
    if isinstance(msg, dict):
        resp = {
            "msg": "数据返回成功",
            "code": 200,
        }
        resp.update(msg)
        return resp
    elif isinstance(msg, list):
        resp = {"msg": "数据返回成功", "code": 200, 'data': msg}
        return resp
    elif isinstance(msg,tuple):
        resp = {"msg": "数据返回成功", "code": 200, 'data': list(msg)}
        return resp
    else:
        resp = {
            "msg": msg,
            "code": 200
        }
        return resp

def error_msg(msg):
    resp = {
        "msg": msg,
        "code": 500
    }
    return resp


def model_to_dict(instance):
    """
    将Django模型实例转换为字典。

    :param instance: Django模型实例。
    :return: 包含模型字段和值的字典。
    """
    if instance is None:
        return None

    # 获取所有字段名
    fields = [field.name for field in instance._meta.fields]
    # 构建字段名和值的字典
    data = {field: getattr(instance, field) for field in fields}
    return data


def queryset_to_dict_list(queryset):
    """
    将Django查询集转换为字典列表。

    :param queryset: Django查询集。
    :return: 包含每个对象字典的列表。
    """
    return [model_to_dict(obj) for obj in queryset]
