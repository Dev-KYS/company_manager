from django.contrib import admin
from .models import MyUser, Team, Agent, Grant

admin.site.register(MyUser)
admin.site.register(Agent)
admin.site.register(Grant)