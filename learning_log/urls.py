
#from django.urls import path
from django.conf.urls import include,url
from django.contrib import admin
#from learning_logs import views as learning_views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'',include('learning_logs.urls',namespace='learning_logs')),
    url(r'^users/', include('users.urls',namespace='users')),
]
