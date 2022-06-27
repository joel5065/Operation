from django.contrib import admin
from django.urls import path, include
from OperationAA.views import login

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',login),
    path('login',login),
    path('dashboard', include('mainApp.urls'))
    
]
