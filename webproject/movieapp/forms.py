from django import forms
from .models import movies

class MovieForm(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','desc','year','img']
