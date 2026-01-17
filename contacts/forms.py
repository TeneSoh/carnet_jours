from django.forms import ValidationError
from typing import Any
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["nom", "prenom", "email", "phone"]
        labels= {
            "nom":"Entrer votre nom",
            "prenom":"Entrer votre prenom",
            "email": "Entrer L'Email",
            "phone": "Entrer votre Numero de telephone"
        }
        widgets = {
            "nom": forms.TextInput(
                attrs={
                    "class": "nom",
                    "id": "nom",
                    "name": "nom",
                    "placeholder": "Entrer votre nom",
                }
            ),
            "prenom": forms.TextInput(
                attrs={
                    "class": "prenom",
                    "id": "prenom",
                    "name": "prenom",
                    "placeholder": "Entrer votre prenomm",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "email",
                    "id": "email",
                    "name": "email",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "phone",
                    "id": "phone",
                    "name": "phone",
                }
            ),
        }

    def clean_nom(self):
        nom:str = str(self.cleaned_data.get('nom'))
        if len(nom) < 4:
            raise ValidationError("Le nom doit etre au moins 4 caracter")
        return nom
    
    def clean_prenom(self):
        prenom:str = str(self.cleaned_data.get('prenom'))
        if len(prenom) < 4:
            raise ValidationError("Le prenom doit etre au moins 4 caracter")
        return prenom

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        phone = str(cleaned_data.get('phone'))
        email = str(cleaned_data.get('email'))
        if len(phone) < 4:
            raise forms.ValidationError({
                'phone': "Entrer le phone number",
            })
        if len(email) < 4:
            raise forms.ValidationError({
                "email" : "Entre l'email"
            })
        return cleaned_data



# nom = forms.CharField(
#     required=True,
#     widget=forms.TextInput(
#         attrs={
#             "class": "",
#             "id": "nom",
#             "name": "nom",
#             "placeholder": "Entrer votre nom",
#         }
#     ),
#     label="Nom :",
# )
# prenom = forms.CharField(
#     required=True,
#     max_length=255,
#     widget=forms.TextInput(
#         attrs={
#             "class": "prenom",
#             "id": "prenom",
#             "name": "prenom",
#             "placeholder": "Entrer votre prenomm",
#         }
#     ),
# )
# email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
#     "class": "email",
#     "id": "email",
#     "name": "email",
# }))
# phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
#     "class": "phone",
#     "id": "phone",
#     "name": "phone",
# }))
# image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
#     "class": "image",
#     "id": "image",
#     "name": "image",
# }))
