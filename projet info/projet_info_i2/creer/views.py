from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Formations, Eleves, Salles, Profs 
from .forms import Data_uploadForm
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def accueil(request):
  template = loader.get_template('00/index.html')
  return HttpResponse(template.render())

def upload_file(request, nom):
  if request.method == 'POST':
        form = Data_uploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                formations, created = Formations.objects.get_or_create(id=row['ID'], nom=row['Nom'], prenom=row['Prénom'], 
                                                                       sexe=row['Sexe'], matiere=row['Matiere'], contrat=row['Contrat'],)
                if created:
                    messages.success(request, f'Successfully imported {Formations.nom}')
                else:
                    messages.warning(request, f'{formations.nom} already exists')
            return redirect('page_11')
  else:
        form = Data_uploadForm()
  return form 
  
def page_11(request):
  file_formation = upload_file(request)
  
  return render(request, '11/index.html', {'form': file_formation})

def page_12(request):
  ''''''
  
  return render(request, '12/index.html')

def page_13(request):
  ''''''
  
  return render(request, '13/index.html')

def page_14(request):
  ''''''
  
  return render(request, '14/index.html')





  
  
  

'''

def eleves(request):
  eleves = Eleves.objects.all().values()
  template = loader.get_template('Eleve.html')
  context = {
    'eleves': eleves,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  eleve = Eleves.objects.get(id=id)
  template = loader.get_template('Profile.html')
  context = {
    'eleve': eleve,
  }
  return HttpResponse(template.render(context, request))

  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))
'''