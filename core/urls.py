from django.contrib import admin
from django.urls import path, include
from chat import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'), 
    
    # 2. Registration
    path('register/', views.register, name='register'),
    
    # 3. Password Reset Logic (Includes 4 sub-urls automatically)
    path('accounts/', include('django.contrib.auth.urls')), 
    
    # 4. Chat App
    path('', views.index, name='index'), 
    path('chat/<slug:slug>/', views.room, name='room'), 
]