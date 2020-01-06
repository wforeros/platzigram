from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect

# Exceptions
from django.db.utils import IntegrityError

# Modelos
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm
from users.forms import SignupForm


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
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = SignupForm()
        
    return render(
        request, 
        'users/signup.html', 
        context={'form': form}
    )



@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(request, 
            'users/update_profile.html',
            context = {
                'profile': profile,
                'user': request.user,
                'form': form
            }
    )