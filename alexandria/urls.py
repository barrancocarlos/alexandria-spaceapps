from django.urls import path
from alexandria import views

urlpatterns = [    
    path('', views.home, name='home'),
    path('nlp/', views.nlp, name='nlp'),
    path('nlp-single/', views.nlpsingle, name='nlpsingle'),
    path('corpus/', views.corpus, name='corpus'), 
    path('video/', views.video, name='video'),      
]