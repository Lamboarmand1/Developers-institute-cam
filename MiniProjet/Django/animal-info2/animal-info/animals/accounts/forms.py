from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register_form(forms.Form):
    image = forms.ImageField(label='Load your profile_image')
    bio = forms.CharField(label='Write your bio')

# class Register_form(forms.Form):
#     class Meta:
#         model=Profile

class UserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password1', 'password2']