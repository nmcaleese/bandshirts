from django.forms import ModelForm
from .models import Shirt

class ShirtForm(ModelForm):
    class Meta:
        model = Shirt
        fields = ['design', 'color', 'size']