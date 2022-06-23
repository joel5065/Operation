


from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return  render(request, "login.html", context={"prenom":"Joel"})