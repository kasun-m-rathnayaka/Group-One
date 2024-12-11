from django.shortcuts import render
from django.http import HttpResponse
from .models import Firm

# Create your views here.
def funding(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        cpm = request.POST['cpm']
        investment = request.POST['investment']
        Firm.objects.create(name=name, cpm=cpm, investment=investment)
    context = {
        'fundings': Firm.objects.all()
    }
    return render(request, 'funding.html', context)


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')