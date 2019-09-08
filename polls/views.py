from django.shortcuts import render
from .models import Sign


def index(request):
    return render(request, 'polls/index.html')

def about(request):
    return render(request, 'polls/about.html', {'title': 'About'})

def database(request):
    context = {
        'signs': Sign.objects.all()
    }
    return render(request, 'polls/database.html', {'title': 'Data'}, context)