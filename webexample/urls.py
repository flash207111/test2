# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('1/', views.index1, name = 'index1'),
    path('2/', views.index2, name = 'index2'),
    path('3/', views.index3, name = 'index3'),
]
