from django.urls import path
from .import views


urlpatterns = [ 

    path('tutorials/', views.tutorials, name = 'tutorials'),
    path('singleTutorial/<str:pk>/', views.singleTutorial, name = 'singleTutorial'),
    path('createTutorial/', views.createTutorial, name='createTutorial'),
    path('updateTutorial/<str:pk>/', views.updateTutorial, name='updateTutorial'),
    path('deleteTutorial/<str:pk>/', views.deleteTutorial, name='deleteTutorial'),

]