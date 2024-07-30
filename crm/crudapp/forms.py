from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Records

from django import forms
from django.forms.widgets import PasswordInput, TextInput


# create/register form
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','password1','password2']

# login user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# create record form
class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Records
        fields = ['first_name','last_name','email','phone','address','country','state','city']


# update record form
class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Records
        fields = ['first_name','last_name','email','phone','address','country','state','city']

    
        
