from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterform


def register(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            #this will creat a new user from the form in the front end 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ure account has been created you are now able to log in!')
            return redirect('users-login')
    else:
        form = UserRegisterform()
    return render(request , 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request ,'users/profile.html')
