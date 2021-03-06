from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('register/', views.register),
    path('success/', views.success),
    path('logout/', views.logout),
]