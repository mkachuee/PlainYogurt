from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
            Create a new user. It takes 3 parameters:
            username
            password1
            password2

            Throw errors in these scenario:
            username already exists in database
            same username and password
            username contains invalid characters (such as !@#$%...)
            password1/password2 too short (<8 characters)
            password1 is not the same as password2
    """

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        if commit:
            user.save()

        return user

    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password1 = forms.CharField(label="Password", max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    password2 = forms.CharField(label="Repeat Password", max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class LoginForm(AuthenticationForm):
    """
                Authenticate a user. It takes 2 parameters:
                username
                password

                Throw errors in these scenario:
                username does not exists in database
                password is wrong
    """
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

