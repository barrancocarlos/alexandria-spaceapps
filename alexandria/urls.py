from django.urls import path
from alexandria import views

urlpatterns = [    
    path('', views.home, name='home'),    
]