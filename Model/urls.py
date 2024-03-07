from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='My_home')

]