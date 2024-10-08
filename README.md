# 环境配置及功能模块说明

## node_modules网盘下载
https://wwd.lanzout.com/iVX0t1p7fnif

## 项目环境

Python3.11.6

Windows11

Pycharm2022.3.3专业版

VSCODE

NODE.JS 20.11.1

Mysql8

后端框架：django

## 后端环境配置

**请确保进行此步骤前，配置好python、Pycharm编辑器与mysql8的环境**
打开Pycharm，打开项目，设置项目解释器为Python3.11.6
在pycharm中打开终端(Ternimal)输入来安装依赖

```python
pip install -r requirements.txt
```

安装依赖完成后，在django_calendar/settings.py中修改数据库连接配置：

<img src="https://immich.lyh27.top/api/assets/a1cf650e-8529-4e46-86b0-14019e014ab8/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221225325906" />

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_calendar', # 数据库名
        'USER': 'root', # 数据库用户名
        'PASSWORD': '123456', # 数据库密码
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
```

使用Navicat等数据库管理工具，创建数据库django_calendar：

<img src="https://immich.lyh27.top/api/assets/3a9ea9dd-92e9-4952-9b30-e2c06fd2e5dd/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221225512985" />

接着打开pycharm中的终端(terminal)，依次输入以下命令进行模型迁移:

```cmd
python manage.py makemigrations
python manage.py migrate
```

最后在pycharm终端中，输入启动django后端服务

```
python manage.py runserver 7000
```

后端接口地址：127.0.0.1:7000/

## 前端环境配置

打开VSCODE，在VSCODE中打开前端项目文件夹，接着，在界面最上方点击终端，选择新建终端，如图

<img src="https://immich.lyh27.top/api/assets/34dcf8ad-4556-4c88-a123-e79b4e1078b6/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221225911288" />

```shell
运行
npm run serve
```

出现以下即为运行前端成功

<img src="https://immich.lyh27.top/api/assets/99c04430-8645-4add-a8d4-357fbfcf6f88/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221225956353" />

前端运行地址：127.0.0.1:8080/

## 模块介绍

### 用户注册登录模块

第一次启动项目，数据库中没有数据，需要注册一个管理员用户。进入前端页面，如图所示进行注册：

<img src="https://immich.lyh27.top/api/assets/95e9ad36-a2b0-4f59-8f16-319db39b077b/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221230103246" />

默认注册的用户为普通用户，第一次需要到数据库表中，修改role字段值为1即为修改为管理员

<img src="https://immich.lyh27.top/api/assets/966dad7f-c22c-426b-8224-8572a700beea/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221230240062" />

然后进行登录

<img src="https://immich.lyh27.top/api/assets/2577cd5b-46c8-4485-af35-501d74f37af5/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221230334937" />

### 电子日历模块

#### 视图切换功能

右上角的月、周、天，分别为切换月视图、周视图、天视图。左上角切换前后月份、周、天。

<img src="https://immich.lyh27.top/api/assets/841aa4a7-59a3-4fdf-90d7-3fa5ef890b08/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221230435776" />

周视图效果

<img src="https://immich.lyh27.top/api/assets/f653385b-2341-4b36-a4e4-3f399be2c73a/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221231547331" />

<img src="https://immich.lyh27.top/api/assets/bd02f6bc-2aba-4cd4-88f4-45e84dbef681/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221231602062" />

月视图效果

<img src="https://immich.lyh27.top/api/assets/b7644dc9-9482-4a61-8e47-ed25977e3fbc/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221231633920" />

#### 事件创建

点击日期可添加自定义事件，可以新建事件名称、开始时间、事件持续时间、事件发生地点、事件描述等

<img src="https://immich.lyh27.top/api/assets/fe0fc500-b332-4590-86b8-c22c23afccd2/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221230653961" />

#### 重复事件

当勾选重复事件时，可设置该事件为重复性事件，可以为年事件、月事件以及周事件的，重复类型意思是每周发生、每月发生、每年发生。重复间隔的意思是重复事件发生之间的间隔，结束时间如果为空，则为永久性重复事件。例如周重复事件的重复间隔为2，结束时间为空，那么就会永远的每两周发生一次事件。

<img src="https://immich.lyh27.top/api/assets/eb7e9f1a-8628-4217-8df8-9f374c9a3e36/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221230802465" />

点击已有的事件可以对事件进行编辑操作

<img src="https://immich.lyh27.top/api/assets/6c8ee6df-bc8c-4d01-ab2a-b7eef662aff3/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221231216962" />

<img src="https://immich.lyh27.top/api/assets/b0d6f7f7-d40d-44ba-a6fd-edab711bbc73/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221231226749" />

可以同一天不同时间段定义不同事件

<img src="https://immich.lyh27.top/api/assets/164e11b4-5c04-40c0-89fb-469677681344/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221231846881" />

当事件事件超过当天24小时，则第二天也会显示进行中的事件，设置事件开始时间为当天20:00，持续时间为10小时

<img src="https://immich.lyh27.top/api/assets/e9ee4087-30db-4b48-8b31-362bc1fe6b31/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232025298" />

<img src="https://immich.lyh27.top/api/assets/566cde1c-4b5c-444c-9fc8-6a736c33f030/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232043695" />

<img src="https://immich.lyh27.top/api/assets/a19467c3-8cfd-4dfc-a82d-bbec2ed99e24/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232055662" />

一天内事件较多时，可对事件进行折叠与展开

<img src="https://immich.lyh27.top/api/assets/8b94bb6d-4e0e-4126-b50f-018a8d4cf4a7/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-202402212322189" />

<img src="https://immich.lyh27.top/api/assets/a1ef7fe8-b401-4bc1-930f-5c8a4c9bd7d8/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232227785" />

### 提醒模块

系统会在事件开始前半个小时弹出提示“xx活动即将开始”，事件进行中弹出提示“xx活动已经开始”。

<img src="https://immich.lyh27.top/api/assets/a3011539-a1fb-4386-a734-9542d30881cb/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232542476" />

<img src="https://immich.lyh27.top/api/assets/b9e4ee3c-5621-4eab-a13f-1c15cc4a2c15/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232607323" />

### 用户管理

该模块只有以管理员身份登录时才显示到菜单栏上，可对用户进行信息修改，同时可以进行用户名的模糊查询以及账户封禁功能

<img src="https://immich.lyh27.top/api/assets/5d1fbf4e-09f9-40a3-b287-5b4892f95a37/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232812826" />

<img src="https://immich.lyh27.top/api/assets/8483b7b5-2a3e-4705-9919-739aecb41eb9/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232906427" />

### 事件管理

该模块只有以管理员身份登录时才显示到菜单栏上，可对不同用户所拥有的日程事件安排进行管理，同时可以进行事件标题的模糊查询

<img src="https://immich.lyh27.top/api/assets/18857a09-215f-4ae3-b131-b3a3a45b6fec/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8" alt="image-20240221232959451" />

![image-20240221233015129](https://immich.lyh27.top/api/assets/81273e51-cf58-4180-931e-e57a270e6b4d/thumbnail?size=preview&key=25V6Vu9F_RRr2dJRHv9neJzgAYlcc4v8m9nc51VCXZcwhXYMn8GwtfaJuVsBitUCJq8)
