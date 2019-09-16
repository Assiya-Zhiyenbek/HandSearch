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
    return render(request, 'polls/database.html', context, {'title': 'Database'})

def byhand(request):
    return render(request, 'polls/byhand.html', {'title':'ByHand'})

def bytyping(request):
    return render(request, 'polls/bytyping.html', {'title': 'ByTyping'})
