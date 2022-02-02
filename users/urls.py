from django.urls import path
from .import views



urlpatterns = [ 
    path('userLogin', views.userLogin, name='userLogin' ),
    path('userRegister', views.userRegister, name='userRegister' ),
    path('userLogout', views.userLogout, name='userLogout'),
    

    path('profile', views.profile, name='profile'),
    path('singleProfile/<str:pk>/', views.singleProfile, name='singleProfile'),

    path('account', views.userAccount, name='account'),
    path('account', views.createAccount, name='createAccount'),
    path('updateAccount', views.updateAccount, name='updateAccount'),

    path('inboxMessage', views.inboxMessage, name='inboxMessage'),
    path('sendMessage/<str:pk>/', views.sendMessage, name='sendMessage'),
    path('viewMessage/<str:pk>/', views.viewMessage, name='viewMessage'),

    
]