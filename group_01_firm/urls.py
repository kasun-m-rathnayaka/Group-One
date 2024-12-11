from django.urls import path
from . import views

urlpatterns = [
    path('funding/', views.funding, name='funding'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('history/<int:pk>', views.history, name='history'),

]