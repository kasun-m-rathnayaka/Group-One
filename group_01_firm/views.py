from django.shortcuts import render
from django.http import HttpResponse
from .models import Firm
from django.shortcuts import get_object_or_404

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


def history(request,pk):
    data = Firm.objects.all()
    context = {
        'context': data
    }
    print(context)
    return render(request, 'history.html', context)


def consultent1(request):
    return render(request, 'consultant1.html')

def consultent2(request):
    return render(request, 'consultant2.html')

def consultent3(request):
    return render(request, 'consultant3.html')