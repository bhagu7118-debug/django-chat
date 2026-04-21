from django.contrib import admin
from django.urls import path, include
from chat import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Registration (Your custom view)
    path('register/', views.register, name='register'),
    
    # 2. Authentication "Power Pack"
    # This single line handles: 
    # - login/ (at /accounts/login/)
    # - logout/ (at /accounts/logout/)
    # - ALL Password Reset logic
    path('accounts/', include('django.contrib.auth.urls')), 
    
    # 3. Custom Logout (If you want your specific redirect logic)
    path('logout/', views.logout_view, name='logout'), 
    
    # 4. Chat App
    path('', views.index, name='index'), 
    path('chat/<slug:slug>/', views.room, name='room'), 
]