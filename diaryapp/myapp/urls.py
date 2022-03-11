from django.urls import path, re_path
from . import views

from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('diary/<str:id>', views.diary, name='diary'),
    path('add', views.add, name='add'),
   
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    path('signup', views.signup, name='signup'),
]

 #path('signin', views.signin, name='signin'),