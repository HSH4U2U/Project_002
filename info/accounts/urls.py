<<<<<<< HEAD
from django.urls import path, re_path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.view_logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
=======
from django.urls import path, re_path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.view_logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
>>>>>>> bfc488ad51715cf21e4e02fbe4765263f013a6aa
]