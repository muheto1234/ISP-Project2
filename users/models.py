from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_directeur=models.BooleanField(default=False)
    is_commandant=models.BooleanField(default=False)
    is_secraiteur=models.BooleanField(default=False)
    
class registeruser(models.Model):
    
    grade=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email=models.EmailField(default=True)
    matricule=models.CharField(max_length=50, primary_key=True)
    image=models.ImageField(upload_to='img',blank=True)
    promotion=models.CharField(max_length=50)
    commandant_promotion=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    password=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)

    def __str__(self) :
        return self.nom
    

class cop(models.Model):
    demandeur = models.ForeignKey(registeruser, on_delete=models.CASCADE, blank=True,default=None)
    motif=models.TextField()
    date=models.DateField(auto_now_add=True)
    date_aller=models.DateField(blank=True)
    date_retour=models.DateField(blank=True)
    signe=models.BooleanField(default=False)

    def __str__(self):
        return self.demandeur.nom
   

class reponse(models.Model):
    Cop=models.ForeignKey(cop,on_delete=models.CASCADE)
    accords=models.TextField()
    date_aller=models.DateField(default=True)
    date_retour=models.DateField(default=True)
    
    def __str__(self):
        return str(self.Cop)
