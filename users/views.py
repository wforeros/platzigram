from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views 


from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy


# Exceptions
from django.db.utils import IntegrityError

# Modelos
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

# Forms
from users.forms import ProfileForm
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    
    template_name='users/detail.html'
    slug_field='username'
    # Este nombre es el que está en la url, sale <str:username>
    slug_url_kwarg='username'
    queryset=User.objects.all()
    context_object_name='user'

    # Para agregar los posts sobre escribiremos el metodo get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LoginView(auth_views.LoginView):
    """
    Esta clase ya contiene un formulario
    por tanto los errores son enviados dentro de este
    y se leen con form.errors
    """

    template_name = 'users/login.html'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirige a la url con nombre feed (urls.py)
            return redirect('posts:feed')
            
        else:
            # Return an 'invalid login' error message.
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')

class LogoutView(auth_views.LogoutView):
    pass

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

class SignupView(FormView):
    template_name='users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

# Forma usando vistas basadas en clases, en este caso UpdateView, así ya no se necesita
# ProfileForm
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view"""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile"""
        username = self.request.user.username
        return reverse('users:detail', kwargs={'username': username})

# Forma normalita con un método
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
            
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
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