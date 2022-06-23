
from django.urls import path

from mainApp.views import homepage



urlpatterns = [

    path('', homepage, name="main-view")

]
