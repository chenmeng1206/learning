from django.urls import path,include
from django.contrib.auth.views import LoginView #导入默认登录视图
from django.conf.urls import url

from . import views
LoginView.template_name='users/login.html'
urlpatterns =[
   #登录界面
    path('login/',LoginView.as_view(),name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'register/$', views.register, name='register'),
]
app_name = "users"