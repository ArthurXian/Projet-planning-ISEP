from django.db import models
from import_export import resources

# Create your models here.
class Salles(models.Model):
    campus = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key= True)
    type = models.CharField(max_length=255)
    
    def __str__(self):
        return self.id
    
class Formations(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    anne_bac = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
        
    def __str__(self):
        return  self.id 
    
class Modules(models.Model):
    nom = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key= True)
    heures = models.CharField(max_length=255)
    
    def __str__(self):
        return self.id 
    
class SModules(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    nom = models.CharField(max_length=255)
    heures = models.CharField(max_length=255)
    
class Classes(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    nom = models.CharField(max_length=255)
    id_formation = models.CharField(max_length=255)
    
    def __str__(self):
        return self.id
    
class Eleves(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    formation = models.CharField(max_length=255)
    option = models.CharField(max_length=255)
    
    def __str__(self):
        return self.id


class Profs(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    matiere = models.CharField(max_length=255)
    contrat = models.CharField(max_length=255)
    
    def __str__(self):
        return self.id
    
class Calendar(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    
    def __str__(self):
        return self.id
    
class Nouveau(models.Model):
    nom = models.CharField(max_length=255, primary_key=False)
    s_et_anne = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom
    

    
  
    
# python3 manage.py makemigrations creer
# python3 manage.py migrate
# python3 manage.py shell
# Formations.objects.all().values()
'''
>>> from members.models import Member
>>> x = Member.objects.all()[0]
>>> x.phone = 5551234
>>> x.joined_date = '2022-01-05'
>>> x.save()
'''