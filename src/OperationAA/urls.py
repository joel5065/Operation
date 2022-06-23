from django.contrib import admin
from django.urls import path, include
from OperationAA.views import login

urlpatterns = [
    #path('', login, name="login"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('home/',include("mainApp.urls")),
    
]
