from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect


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
