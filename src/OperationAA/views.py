from django.contrib import messages
from django.shortcuts import  redirect, render
from django.contrib.auth.forms import UserCreationForm



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Compte Cree')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html', {'form':form})


def login(request):
    return render(request,'login.html')


# def login(request):
#     form = loginForm()

#     if request.method == 'POST':
#         form = loginForm(request.POST)
#         if form.is_valid:
#             return redirect('dashboard')

#     context ={'form':form}
#     return render(request, 'login.html',context)