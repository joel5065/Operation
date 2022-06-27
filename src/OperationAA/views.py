from django.shortcuts import redirect, render


def login(request):
    error = " Veuillez rentrez un nom utilisateur et un mot de passe correct "
    if len(request.POST) > 0:   # verifie si il y a une entree
        if 'username' not in request.POST or 'password' not in request.POST:
            return render(request, 'login.html',{'error': error})
        else:
            username = request.POST['username']
            
            password = request.POST['password']

            if password != 'Joel@2019' or username != 'joel':
                return render(request,'login.html',{'error': error})
            else:
                redirect('dashboard')
    else:
        return render(request,'login.html')