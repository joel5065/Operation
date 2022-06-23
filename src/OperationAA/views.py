


from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render



def login(request):
    return  render(request, "OperationAA/login.html", context={"prenom":"Joel"})