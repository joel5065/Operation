from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> La Situation Technique</h1>")