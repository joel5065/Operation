from django.contrib import admin
from django.urls import path, include
from OperationAA.views import login, register

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login',login),
    path('register', register),
    path('', include('mainApp.urls'))
    
]
