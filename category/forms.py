from django import forms
from .models import Category

class CategoryFilterForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id', 'title']