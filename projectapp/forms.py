# projectapp/forms.py
from django import forms
from .models import YourModel

class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = '__all__'