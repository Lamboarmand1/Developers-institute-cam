from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.home, name='home'),
    path('addFilm/', views.addfilm, name='addfilm'),
    path('addDirector/', views.addDirector, name='adddirector')
]