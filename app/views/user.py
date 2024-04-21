import json
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from app.forms import UserRegistrationForm
from app.utils.message import *
from app.models import *
from django.middleware.csrf import get_token
import jwt
def csrf_token(request):
    csrfToken = get_token(request)
    return JsonResponse({'csrfToken': csrfToken})


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = UserRegistrationForm(data)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            # 处理注册逻辑（如自动登录等）
            return JsonResponse(success_msg("注册成功"))
        else:
            print(form.errors)
            return JsonResponse(error_msg("注册失败"))


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        username = data.get('username')
        password = data.get('password')
        user = UserInfo.objects.filter(username=username).first()
        if user.status == 0:
            return JsonResponse(error_msg("用户已被禁用"))
        if user and check_password(password, user.password):
            if 'user_id' in request.session:
                return JsonResponse(error_msg("请勿重复登录"))
            else:
                request.session['user_id'] = user.id
                # 确保会话数据被保存
                request.session.modified = True
                # 生成 JWT token
                token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(days=7)}, 'SECRET_KEY',
                                   algorithm='HS256')
                data = {
                    'user_id': user.id,
                    'role': user.role,
                    'token': token
                }
                return JsonResponse(success_msg(data))
        else:
            return JsonResponse(error_msg("用户名或密码错误"))
    else:
        # 如果不是 POST 请求，返回错误信息
        return JsonResponse(error_msg("无效的请求"))

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # 清除session
        return JsonResponse(success_msg("账户登出成功"))
    else:
        return JsonResponse(error_msg("账户已经登出,请勿重复登出"))

def get_user(request):
    if request.method == 'POST':    # 搜索
        data = json.loads(request.body)
        username = data.get('username')
        user = UserInfo.objects.filter(username__icontains=username).all()
        data_dict = queryset_to_dict_list(user)
        if user:
            return JsonResponse(success_msg(data_dict))
        else:
            return JsonResponse(error_msg("用户不存在"))
    else:
        user = UserInfo.objects.filter().all()
        data_dict = queryset_to_dict_list(user)
        return JsonResponse(success_msg(data_dict))
def update_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        username = data.get('username')
        email = data.get('email')
        role = data.get('role')
        status = data.get('status')
        UserInfo.objects.filter(id=user_id).update(
            username=username,
            email=email,
            role=role,
            status=status
        )
        return JsonResponse(success_msg(f"修改用户id:{user_id}成功"))
    else:
        return JsonResponse(error_msg("无效的请求"))