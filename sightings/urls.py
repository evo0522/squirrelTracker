from django.urls import path

from . import views

urlpatterns = [
    #/sightings, A view that lists all squirrel sightings with links to edit and add sightings
    path('', views.list, name='list'),





    path('<str:st_id>/', views.single, name='squirrel'),

]
