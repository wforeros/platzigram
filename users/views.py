from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect

# Exceptions
from django.db.utils import IntegrityError

# Modelos
from django.contrib.auth.models import User
from users.models import Profile


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirige a la url con nombre feed (urls.py)
            return redirect('feed')
            
        else:
            # Return an 'invalid login' error message.
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

        
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirmation']
        if password != password_confirm:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
        try:
            user = User.objects.create_user(username, password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already registered'})
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()
        return redirect('login')
    return render(request, 'users/signup.html')