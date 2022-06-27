
from django.urls import path
from mainApp.views import dashboard



urlpatterns = [
        
        path('dashboard', dashboard, name="dashboard"),
    
]