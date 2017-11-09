from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^lists/', views.userlist, name='userlist'),
    url(r'^detail/', views.userdetail, name='userdetail'),
]
