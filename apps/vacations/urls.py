from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^lists/', views.vacation_list, name='vacation_list'),
    url(r'^mylist/', views.vacation_mylist, name='vacation_mylist'),
    url(r'^teamlist/', views.vacation_teamlist, name='vacation_teamlist'),
    url(r'^create/', views.vacation_create, name='vacation_create'),
    url(r'^detail/', views.vacation_detail, name='vacation_detail'),
    url(r'^agree/', views.agree, name='vacation_agree'),
    url(r'^denied/', views.denied, name='vacation_denied'),
    url(r'^vacation_check', views.vacation_check, name='vacation_check'),
    url(r'^select_users', views.select_users, name='select_users'),
]
