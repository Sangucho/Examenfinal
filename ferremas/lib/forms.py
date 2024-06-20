import attrs
from django import forms
CHOICES =(
    ("amplificador", "amplificador"),
    ("bateria", "bateria"),
    ("guitarra electrica", "guitarra electrica"),
    ("guitarra", "guitarra"),
    ("piano", "piano"),
    ("trompeta", "trompeta"),
    ("violin", "violin"),
)

class PrductoForm(forms.Form):
    nombre = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.Select(attrs={'class': "form-select"}))
    descripcion = forms.CharField(required=True,min_length=3, max_length=150, widget=forms.TextInput(attrs={'class': "form-control"}))
    precio = forms.IntegerField(required=True,min_value=0,widget=forms.NumberInput(attrs={'class': "form-control"}))
    stock = forms.IntegerField(required=True,min_value=0,widget=forms.NumberInput(attrs={'class': "form-control"}))