from django.conf.urls import url

from main import views

app_name = "main"
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register-result/$', views.register_result, name='register-result'),
    url(r'^login-action/$', views.login_action, name='login-action'),
    url(r'^logout/$', views.logout_action, name='logout'),
]
