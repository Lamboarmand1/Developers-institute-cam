from django import forms
from django.forms import TextInput

from .models import Animals

class AddAnimalForm(forms.ModelForm):
    class Meta:
        model = Animals
        exclude= ['owner'] #the form will take all the fields except owner
        labels={'name':'Animal Name'} #adding labels
        widgets= {
            'name': TextInput(attrs={
                'placeholder': 'Enter the name of the animal',
            })
        }

