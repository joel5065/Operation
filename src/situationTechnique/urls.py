

from django.urls import path
from situationTechnique.views import index


urlpatterns = [

    path('', index, name="blog-index")

]
