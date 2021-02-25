from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('links/', views.LinkPage, name='links'),
]
