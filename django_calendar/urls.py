# from django.contrib import admin
from django.urls import path
from app.views import user,event

urlpatterns = [
    path('register', user.register),
    path('get_csrf', user.csrf_token),
    path('login', user.login),
    path('logout', user.logout),
    path('get_user', user.get_user),
    path('update_user', user.update_user),
    path('add_event', event.add_event),
    path('get_event', event.get_event),
    path('del_event', event.del_event),
    path('update_event', event.update_event),
    path('get_all_events', event.get_all_events),

]
