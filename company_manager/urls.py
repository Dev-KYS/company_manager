from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from apps.users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', auth_views.login, name='login', kwargs={'template_name': 'registration/login.html'}),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page' : '/accounts/login'}),
    url(r'^accounts/signup$', views.signup, name='signup'),
    url(r'^users/', include('apps.users.urls')),
    url(r'^vacations/', include('apps.vacations.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

