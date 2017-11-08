from django.conf.urls import url
from . import views

app_name = "vacation_manager"

urlpatterns = [
    url(r'^vacation_list/', views.Vacation_list, name='vacation_list'),
    url(r'^my_vacation/', views.My_vacation_list, name='my_vacation_list'),
    url(r'^vacation_register/', views.Vacation_register, name='vacation_register'),
    url(r'^vacation_detail/', views.Vacation_detail, name='vacation_detail'),
    url(r'^register_vacation/', views.Register_vacation, name='register_vacation'),
]