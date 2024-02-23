from django.db import models

class UserInfo(models.Model):
    """
        back_userinfo
        用户表
    """
    username = models.CharField(verbose_name='用户名', max_length=32, null=True, blank=False, unique=True)
    password = models.CharField(verbose_name='密码', max_length=255, null=True, blank=False)
    email = models.CharField(verbose_name='邮箱', null=True, max_length=64, unique=True)
    role = models.IntegerField(verbose_name='角色', default=0)
    pic = models.CharField(verbose_name='头像', max_length=300, default='/static/user_default.png')
    status = models.IntegerField(verbose_name='账号状态', default=1)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_time = models.DateTimeField(verbose_name='最后登录时间', auto_now=True)


class EventInfo(models.Model):
    """
        back_eventinfo
        事件表
    """
    title = models.CharField(verbose_name='事件标题', max_length=255, null=True, blank=False)
    area = models.CharField(verbose_name="地点",max_length=255, null=True, blank=False)
    detail = models.CharField(verbose_name="事件内容",max_length=255, null=True, blank=False)
    more = models.BooleanField(verbose_name="是否为周期事件",default=False)
    duration = models.CharField(verbose_name='持续时间', max_length=255, null=True, blank=False)
    user_id = models.IntegerField(verbose_name='该事件对应的用户ID',null=True, blank=False)
    freq = models.CharField(verbose_name='循环周期',max_length=255)
    interval = models.IntegerField(verbose_name='循环间隔')
    dtstart = models.DateTimeField(verbose_name="开始时间")
    until = models.DateTimeField(verbose_name="结束时间",null=True, blank=True)
    count = models.IntegerField(blank=True, null=True,verbose_name="事件次数")
    class Meta:
        verbose_name = "事件"
        verbose_name_plural = "事件"

    def __str__(self):
        return self.title