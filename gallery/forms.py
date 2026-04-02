from django import forms
from .models import Products


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ("image", "title")