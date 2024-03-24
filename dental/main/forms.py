from .models import Artiles
from django.forms import ModelForm, TextInput, DateInput, Textarea



class ArtilesForm(ModelForm):
    class Meta:
        model=Artiles
        fields=['title', 'num', 'address', 'date', 'info']

        widgets={
            'title':TextInput(attrs={
                'class':'form-control'
            }),
            'info': Textarea(attrs={
                'class': 'form-control'
            }),
            'date': DateInput(attrs={
                'class': 'form-control'
            }),
            'address': TextInput(attrs={
                'class': 'form-control'
            }),
            'num': TextInput(attrs={
                'class': 'form-control'
            })
        }