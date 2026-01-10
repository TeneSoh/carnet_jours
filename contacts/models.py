from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
class Contact(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    nom = models.CharField(max_length=255, validators=[MinLengthValidator(2, message="Le nom doit etre superieur a deux caracter")])
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)