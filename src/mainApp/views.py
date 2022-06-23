from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# la vue pour enregister quelqu'un 
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form' : form}
    return render(request,'accounts/register.html', context)

# la vue pour sur laquelle on tombe apres l'enregistrement
def homepage(request):
    return render(request,"mainApp/homepage.html")


def situation_technique(request):
    return render(request,"mainApp/situationTechnique.html")


def operation(request):
    return render(request,"mainApp/operation.html")

def coAir(request):
    return render(request,"mainApp/coAir.html")