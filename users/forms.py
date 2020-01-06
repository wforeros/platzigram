from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()

class SignupForm(forms.Form):

    username = forms.CharField(
        label=False,
        min_length=4, 
        max_length=50, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    
    password = forms.CharField(
        label=False,
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )

    password_confirmation = forms.CharField(
        label=False,
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation'
            }
        )
    )

    first_name = forms.CharField(
        label=False,
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }
        )
    )

    last_name = forms.CharField(
        label=False,
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }
        )
    )

    email = forms.CharField(
        label=False,
        min_length=6, 
        max_length=70, 
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Email'
            }
        )
    )

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify passwords match"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

        return data
    
    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
        


    