from .models import Plane
from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select, CheckboxInput

class PlaneForm(ModelForm):
    class Meta:
        model = Plane
        fields = ['text', 'description', 'price', 'type_plane', 'is_selected']

        widgets = {
            "text": TextInput(attrs={
                'class': 'input_title',
                'placeholder': "Text..."
            }),
            "description": Textarea(attrs={
                'placeholder': "Description"
            }),
            "price": NumberInput(attrs={
                'value': '1',
                'min': '1'

            }),
            'type_plane': Select(attrs={
                'style': "text-align: left;"
            }),

            'is_selected' : CheckboxInput(attrs={
                'type': "checkbox",
                }),  
        }

