# 环境配置及功能模块说明

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

![image-20240221225325906](http://sapic.lyh27.top/static/upload/admin/image-20240221225325906.png)

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

![image-20240221225512985](http://sapic.lyh27.top/static/upload/admin/image-20240221225512985.png)

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

![image-20240221225911288](http://sapic.lyh27.top/static/upload/admin/image-20240221225911288.png)

```shell
运行
npm run serve
```

出现以下即为运行前端成功

![image-20240221225956353](http://sapic.lyh27.top/static/upload/admin/image-20240221225956353.png)

前端运行地址：127.0.0.1:8080/

## 模块介绍

### 用户注册登录模块

第一次启动项目，数据库中没有数据，需要注册一个管理员用户。进入前端页面，如图所示进行注册：

![image-20240221230103246](http://sapic.lyh27.top/static/upload/admin/image-20240221230103246.png)

默认注册的用户为普通用户，第一次需要到数据库表中，修改role字段值为1即为修改为管理员

![image-20240221230240062](http://sapic.lyh27.top/static/upload/admin/image-20240221230240062.png)

然后进行登录

![image-20240221230334937](http://sapic.lyh27.top/static/upload/admin/image-20240221230334937.png)

### 电子日历模块

#### 视图切换功能

右上角的月、周、天，分别为切换月视图、周视图、天视图。左上角切换前后月份、周、天。

![image-20240221230435776](http://sapic.lyh27.top/static/upload/admin/image-20240221230435776.png)

周视图效果

![image-20240221231547331](http://sapic.lyh27.top/static/upload/admin/image-20240221231547331.png)

![image-20240221231602062](http://sapic.lyh27.top/static/upload/admin/image-20240221231602062.png)

月视图效果

![image-20240221231633920](http://sapic.lyh27.top/static/upload/admin/image-20240221231633920.png)

#### 事件创建

点击日期可添加自定义事件，可以新建事件名称、开始时间、事件持续时间、事件发生地点、事件描述等

![image-20240221230653961](http://sapic.lyh27.top/static/upload/admin/image-20240221230653961.png)

#### 重复事件

当勾选重复事件时，可设置该事件为重复性事件，可以为年事件、月事件以及周事件的，重复类型意思是每周发生、每月发生、每年发生。重复间隔的意思是重复事件发生之间的间隔，结束时间如果为空，则为永久性重复事件。例如周重复事件的重复间隔为2，结束时间为空，那么就会永远的每两周发生一次事件。

![image-20240221230802465](http://sapic.lyh27.top/static/upload/admin/image-20240221230802465.png)

点击已有的事件可以对事件进行编辑操作

![image-20240221231216962](http://sapic.lyh27.top/static/upload/admin/image-20240221231216962.png)

![image-20240221231226749](http://sapic.lyh27.top/static/upload/admin/image-20240221231226749.png)

可以同一天不同时间段定义不同事件

![image-20240221231846881](http://sapic.lyh27.top/static/upload/admin/image-20240221231846881.png)

当事件事件超过当天24小时，则第二天也会显示进行中的事件，设置事件开始时间为当天20:00，持续时间为10小时

![image-20240221232025298](http://sapic.lyh27.top/static/upload/admin/image-20240221232025298.png)

![image-20240221232043695](http://sapic.lyh27.top/static/upload/admin/image-20240221232043695.png)

![image-20240221232055662](http://sapic.lyh27.top/static/upload/admin/image-20240221232055662.png)

一天内事件较多时，可对事件进行折叠与展开

![image-20240221232218912](http://sapic.lyh27.top/static/upload/admin/image-20240221232218912.png)

![image-20240221232227785](http://sapic.lyh27.top/static/upload/admin/image-20240221232227785.png)

### 提醒模块

系统会在事件开始前半个小时弹出提示“xx活动即将开始”，事件进行中弹出提示“xx活动已经开始”。

![image-20240221232542476](http://sapic.lyh27.top/static/upload/admin/image-20240221232542476.png)

![image-20240221232607323](http://sapic.lyh27.top/static/upload/admin/image-20240221232607323.png)

### 用户管理

该模块只有以管理员身份登录时才显示到菜单栏上，可对用户进行信息修改，同时可以进行用户名的模糊查询以及账户封禁功能

![image-20240221232812826](http://sapic.lyh27.top/static/upload/admin/image-20240221232812826.png)

![image-20240221232906427](http://sapic.lyh27.top/static/upload/admin/image-20240221232906427.png)

### 事件管理

该模块只有以管理员身份登录时才显示到菜单栏上，可对不同用户所拥有的日程事件安排进行管理，同时可以进行事件标题的模糊查询

![image-20240221232959451](http://sapic.lyh27.top/static/upload/admin/image-20240221232959451.png)

![image-20240221233015129](http://sapic.lyh27.top/static/upload/admin/image-20240221233015129.png)
