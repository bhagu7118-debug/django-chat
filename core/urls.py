from django.contrib import admin
from django.urls import path, include
from chat import views 
from django.contrib.auth import views as auth_views

# FULL COMPLETE CODE FOR URLS.PY

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('register/', views.register, name='register'),
    
    # This line is essential for the password reset link logic
    path('accounts/', include('django.contrib.auth.urls')), 
    
    # Chat App
    path('', views.index, name='index'), 
    path('chat/<slug:slug>/', views.room, name='room'), 
]