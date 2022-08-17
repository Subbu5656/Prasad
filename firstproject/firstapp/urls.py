from django.urls import path
from firstapp import views

urlpatterns = [
    path('home/',views.Home, name='home'),
    path('add/', views.Add, name='new employee'),
    path('main/', views.Main, name='all employees'),
    path('delete/<id>/', views.Del, name='delete employee'),
    path('update/<id>/', views.Update, name='update employee'),
    path('home/<id>/', views.HomeId, name='home1'),
]
