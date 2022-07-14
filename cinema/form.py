from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    username = forms.CharField(label="nickname", required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    password1 = forms.CharField(label="пароль", required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    password2 = forms.CharField(label="повторите пароль", required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    email = forms.EmailField(label="почта", required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    first_name = forms.CharField(label="имя", required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    last_name = forms.CharField(label="фамилия", required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    photo = forms.FileField(label='Photo', required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2", "photo")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.photo = self.cleaned_data['photo']
        print(user.photo, '------------')

        if commit:
            user.save()
            return user
