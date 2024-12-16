from django.test import TestCase

# Create your tests here.

from .models import Formations, Eleves, Profs, Salles


class Data_TestCase(TestCase):
    """les données sont bien enregistrées"""
    def setUp(self):
        Formations.objects.create(id=62977, nom="Louis", prenom= "Dubois", formation= "I2.01")
        Eleves.objects.create(id=62977, nom="Louis", prenom= "Dubois", formation= "I2.01")
        Profs.objects.create(id=72977, nom="Louis", prenom= "Dubois", matiere= "BS.101", sexe= "F", contrat="temps plein")
        Salles.objects.create(salle="N34", campus="Lorette_Issy")

    def test_insertion_data(self):
        
        prof = Profs.objects.get(nom="Louis")
        eleve = Eleves.objects.get(prenom="Dubois")
        
        
        self.assertEqual(prof.prenom(), 'Dubois')
        self.assertEqual(eleve.nom(), 'Louis')
        
class HomeView_TestCase(TestCase):
    """les interface sont bien afficher"""
    def setUp(self):
        return None 
        
#$ ./manage.py test 
# Run all the tests in the animals.tests module
#$ ./manage.py test animals.tests