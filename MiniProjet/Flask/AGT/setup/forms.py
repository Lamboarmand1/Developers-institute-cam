from django import forms
from setup.models import Task


class FormTask(forms.ModelForm):
    tache = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Entrer votre tache',
                                                                          'class': 'from-control .from-control-lg'}))

    class Meta:
        model = Task
        fields = ['tache']