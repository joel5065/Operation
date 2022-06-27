from django.shortcuts import render

# la vue pour sur laquelle on tombe apres l'enregistrement ou apres la connexion
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