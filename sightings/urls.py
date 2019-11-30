from django.urls import path

from . import views

urlpatterns = [
    #/sightings, A view that lists all squirrel sightings with links to edit and add sightings
    path('', views.list, name='list'),
    #/sightings/add, A view to create a new sighting
    path('add/', views.add, name='add'),
    path('add_sighting_from_submission/', views.add_sighting_from_submission, name='add_sighting_from_submission'),
    #/sightings/<unique-squirrel-id>, A view to update a particular sighting
    path('<str:sq_id>/', views.single, name='squirrel'),
]
