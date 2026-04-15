from django.contrib import admin
from django.urls import path, include
from chat import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    # MOVE THIS LINE HERE (Above accounts)
    path('logout/', views.logout_view, name='logout'), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('register/', views.register, name='register'),
    path('', views.index, name='index'), 
]