from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import messages
from . import tools

def home(request) :
    return render(request,'users/index.html')   

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        birthday = request.POST.get('birthday', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        country = request.POST.get('country', '')
        residence_location = request.POST.get('residence_location', '')

        user, errors = tools.create_user_with_validation(
            first_name, last_name, birthday, email, password, phone, country, residence_location
        )
        if user is not None:
            user.save()
            login(request, user)
            messages.success(request, "Welcome :)")
            return redirect('home')
        else:
            for error in errors:
                messages.error(request, error)
            return redirect('register')
    else:
        return render(request, 'users/signup.html')
