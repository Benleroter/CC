from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ClientProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ['fullname','branch','contact1', 'contact1tel','contact1email','contact2','contact2tel','contact2email','image']
        labels = {
        'fullname' : 'Company name',
        'branch' : 'Branch/Office',
        'contact1' : 'Contact 1',
        'contact1tel':'Tel no:',
        'contact1email': 'Email',
        'contact2' : "Contact 1",
        'contact2tel':'Tel no:',
        'contact2email': 'Email'
        }


class ProfileUpdateForm2(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ['image']        