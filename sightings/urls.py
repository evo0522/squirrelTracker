from django.urls import path

from . import views

urlpatterns = [
    #/sightings, A view that lists all squirrel sightings with links to edit and add sightings
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('add_sighting_from_submission/', views.add_sighting_from_submission, name='add_sighting_from_submission'),




    path('<str:st_id>/', views.single, name='squirrel'),

]
