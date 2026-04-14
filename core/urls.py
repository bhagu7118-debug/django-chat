from django.contrib import admin
from django.urls import path, include
from chat import views  # Ensure this import is there

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    # ADD THIS LINE BELOW FOR THE HOME PAGE
    path('', views.index, name='index'), 
]