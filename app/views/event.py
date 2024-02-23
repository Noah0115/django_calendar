import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt

from app.forms import UserRegistrationForm
from app.utils.message import *
from app.models import *
from django.middleware.csrf import get_token
from django.core import serializers

def add_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        title = data.get('title')
        area = data.get('area')
        detail = data.get('detail')
        more = data.get('more')
        duration = data.get('duration')
        user_id = data.get('user_id')
        rrule = data.get('rrule')
        freq = rrule.get('freq')
        interval = rrule.get('interval')
        dtstart = rrule.get('dtstart')
        until = rrule.get('until')
        count = rrule.get('count')
        event = EventInfo(title=title, area=area, detail=detail, more=more, duration=duration, user_id=user_id, freq=freq, interval=interval, dtstart=dtstart, count=count,until=until)
        event.save()
        return JsonResponse(success_msg("添加成功"))
    else:
        # 如果不是 POST 请求，返回错误信息
        return JsonResponse(error_msg("无效的请求"))

# @login_required
@csrf_exempt
def get_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        event = EventInfo.objects.filter(user_id=user_id).all()
        data = []
        for obj in event:
            data_dict = {
                'id': obj.id,
                'title': obj.title,
                'area': obj.area,
                'detail': obj.detail,
                'more':obj.more,
                'duration':obj.duration,
                'rrule':{
                    'freq':obj.freq,
                    'interval':obj.interval,
                    'dtstart':obj.dtstart,
                    'until':obj.until,
                    'count':obj.count
                }
            }
            data.append(data_dict)
        # data = queryset_to_dict_list(event)
        # print(data)
        return JsonResponse(success_msg(data))
    else:
        # 如果不是 POST 请求，返回错误信息
        return JsonResponse(error_msg("无效的请求"))

@csrf_exempt
def del_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event_id = data.get('id')
        EventInfo.objects.filter(id=event_id).delete()
        return JsonResponse(success_msg(f"删除事件ID:{event_id}成功"))
    else:
        # 如果不是 POST 请求，返回错误信息
        return JsonResponse(error_msg("无效的请求"))


@csrf_exempt
def update_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event_id = data.get('id')
        # 直接使用更新逻辑，不处理日期时间转换
        updated_count = EventInfo.objects.filter(id=event_id).update(
            title=data.get('title'),
            area=data.get('area'),
            detail=data.get('detail'),
            more=data.get('more'),
            duration=data.get('duration'),  # 确保这里的字段名与模型中定义的匹配
            user_id=data.get('user_id'),
            freq=data.get('rrule', {}).get('freq'),
            interval=data.get('rrule', {}).get('interval'),
            dtstart=data.get('rrule', {}).get('dtstart'),  # 直接使用字符串值
            until=data.get('rrule', {}).get('until'), # 直接使用字符串值
            count = data.get('rrule', {}).get('count')
        )
        if updated_count:
            # 如果有记录被更新，返回成功信息
            return JsonResponse(success_msg(f"修改事件ID:{event_id}成功"))
        else:
            # 如果没有记录被更新，可能是因为没有找到对应的记录
            return JsonResponse(error_msg(f"事件ID:{event_id}未找到或无更新"))

    else:
        # 如果不是POST请求，返回错误信息
        return JsonResponse(error_msg("无效的请求"))

def get_all_events(request):
    if request.method == 'GET':
        events = EventInfo.objects.filter().all()
        data = queryset_to_dict_list(events)
        return JsonResponse(success_msg(data))
    else:
        data = json.loads(request.body)
        title = data.get('title')
        events = EventInfo.objects.filter(title__icontains=title).all()
        data_dict = queryset_to_dict_list(events)

        if events:
            return JsonResponse(success_msg(data_dict))
        else:
            return JsonResponse(error_msg("事件不存在"))
