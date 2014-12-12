from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def sign_out(request):
    logout(request)
    return redirect('/')

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            return redirect('accounts:sign_in')
        else:
            return redirect('/')
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/sign_in.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']

            new_user = authenticate(username=username, password=password)

            login(request, new_user)
            return redirect("index")
        else:
            return redirect("index")
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)