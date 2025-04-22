from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from blog import views_register # Import views_register
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog_list'), name='logout'),
    path('register/', views_register.register, name='register'), # Use views_register.register
    path('', include('blog.urls')),
    path('home/', blog_views.blog_list, name='home'),
]