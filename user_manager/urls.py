from django.conf.urls import url
from . import views

app_name = "user_manager"

urlpatterns = [
    url(r'^list/', views.UserList, name='user_list'),
    url(r'^detail/', views.UserDetail, name='user_detail'),
    url(r'^my_info/', views.MyInfo, name='my_info'),
    url(r'^user_modify/', views.UserInfoModify, name='user_modify')
]