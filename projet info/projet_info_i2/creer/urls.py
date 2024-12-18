from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('creer/', views.accueil, name='accueil'),
    path('creer/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),   
]