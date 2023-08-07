from django.urls import path, include
from . import views

#  URLConf
urlpatterns = [
    path('', views.get_landing, name = 'home'),
    
]