from django.shortcuts import  render
from django.contrib.auth.forms import UserCreationForm


def login(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request,'login.html',context)


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request,'register.html', context)




# def login(request):
#     form = loginForm()

#     if request.method == 'POST':
#         form = loginForm(request.POST)
#         if form.is_valid:
#             return redirect('dashboard')

#     context ={'form':form}
#     return render(request, 'login.html',context)