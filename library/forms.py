from django import forms
from django.forms  import ModelForm
from .models import Books

class bookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        exclude = ['record_updated']
        widgets = {
            'name':forms.TextInput(attrs={"class":"form-control"}),
            'genre':forms.TextInput(attrs={"class":"form-control"}),
            'author':forms.TextInput(attrs={"class":"form-control"}),
            'body':forms.Textarea(attrs={"class":"form-control"}),
        }