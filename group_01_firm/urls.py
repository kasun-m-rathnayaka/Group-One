from django.urls import path
from . import views

urlpatterns = [
    path('funding/', views.funding, name='funding'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('history/<int:pk>', views.history, name='history'),
    path('consultant1', views.consultent1, name='consultant1'),
    path('consultant2', views.consultent2, name='consultant2'),
    path('consultant3', views.consultent3, name='consultant3'),

]