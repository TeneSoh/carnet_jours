from django.forms import fields, widgets
from django import forms 
from .models import Contact
from typing import Any




# UNE AUTRE FACON DE FAIRE EN EXPLOITANT LES CLASSES MODELES



class ContactForm(forms.ModelForm):
   class Meta:
        model = Contact
        fields = [ 'nom', 'prenom' ,'phone' , 'email']
        labels ={
            'nom':"Entrer Votre Nom",
            "prenom":"Entrer Votre Prenom",
            "email":"Entrer Votre Email",
            "phone":"Entrer Votre Tel",
        }

        widgets = {
            "Nom": forms.TextInput(
                  attrs={
                    "class": "nom",
                    "id":"nom",
                    "name":"nom",
                    "placeholder":"Envter votre nom"
                    }
            ),

            "prenom":forms.TextInput(
                attrs={
                    "class": "prenom",
                    "idom":"prenom",
                    "surname":"prenom",
                    "placeholder":"Envter votre prenom" 
                }
            ), 

            "Phone":forms.TextInput(
                attrs={
                     "class": "phone",       
                     "idom":"phone",
                    "surname":"phone",
                    "placeholder":"Envter votre phone"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "email",
                    "idom":"email",
                    "surname":"email",       
                    "placeholder":"Envter votre email"
                }
            )
            
        }


def clean_nom(self):
    pass         
    
       
    

# class ContactForm(forms.Form):

#     nom = forms.CharField(required=True, max_length=255 , widget=forms.TextInput(
#          attrs={
#         "class": "nom",
#         "id":"nom",
#         "name":"nom",
#         "placeholder":"Envter votre nom"
#     }

#     ), label="Nom:")

#     prenom = forms.CharField(required=True , max_length=255 , widget=forms.TextInput(
#         attrs={
#              "class": "prenom",
#             "idom":"prenom",
#             "surname":"prenom",
#             "placeholder":"Envter votre prenom"
#         }
#     ) , label="Prenom :")

#     email = forms.EmailField(required=True , widget=forms.EmailInput(
#         attrs={
#             "class": "email",
#             "idom":"email",
#             "surname":"email",
#             "placeholder":"Envter votre email"
#         }
#     ) , label="Email:")

#     phone = forms.CharField(required=True , widget=forms.TextInput(
#         attrs={
#              "class": "phone",
#             "idom":"phone",
#             "surname":"phone",
#             "placeholder":"Envter votre phone"
#         }
#     ) , label="Phone :")

#     image = forms.ImageField(required=True , widget=forms.FileInput(
#         attrs={
#              "class": "image",
#             "idom":"image",
#             "surname":"image",
#             "placeholder":"Envter votre image"
#         }
#     ) , label="Image")