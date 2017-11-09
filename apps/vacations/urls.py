from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^lists/', views.vacation_list, name='vacation_list'),
    url(r'^mylist/', views.vacation_mylist, name='vacation_mylist'),
    url(r'^teamlist/', views.vacation_teamlist, name='vacation_teamlist'),
    url(r'^create/', views.vacation_create, name='vacation_create'),
    url(r'^detail/', views.vacation_detail, name='vacation_detail'),
]
