from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login/$',views.user_login,name = "user_login"),
    url(r'^logout/$',auth_views.logout,{"template_name":"account/logout.html"},name = "user_logout"),

]
