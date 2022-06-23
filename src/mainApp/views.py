from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

    context = {'form' : form}
    return render(request,'accounts/register.html', context)
def homepage(request):
    return render(request,"mainApp/homepage.html")


def situation_technique(request):
    return render(request,"mainApp/situationTechnique.html")


def operation(request):
    return render(request,"mainApp/operation.html")

def coAir(request):
    return render(request,"mainApp/coAir.html")