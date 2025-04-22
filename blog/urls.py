from django.urls import path
from . import views
from . import views_register

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('register/', views_register.register, name='register'),
]