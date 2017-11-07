from django.conf.urls import url
from . import views

app_name = "user_manager"

urlpatterns = [
    url(r'^list/', views.UserList, name='user_list'),
    url(r'^detail/', views.UserDetail, name='user_detail'),
]