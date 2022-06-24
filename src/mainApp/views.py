from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


# la vue pour enregister quelqu'un 
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        context = {'form' : form}
    return render(request,'accounts/register.html', context)

# la vue pour sur laquelle on tombe apres l'enregistrement
def dashboard(request):
    return render(request,"mainApp/dashboard.html")


# la vue des differentes fenetres du menu principale: celle-ci dois etre ameliore en une seule vue incluant des cles pour chaque vue

# la vue de la situation technique
def situation_technique(request):
    return render(request,"mainApp/situationTechnique.html")

# la vue des operations 
def operation(request):
    return render(request,"mainApp/operation.html")

# la vue des cellules du COAIR 
def coAir(request):
    return render(request,"mainApp/coAir.html")