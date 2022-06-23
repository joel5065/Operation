from django.shortcuts import render


def homepage(request):
    return render(request,"mainApp/homepage.html")


def situation_technique(request):
    return render(request,"mainApp/situationTechnique.html")


def operation(request):
    return render(request,"mainApp/operation.html")

def coAir(request):
    return render(request,"mainApp/coAir.html")