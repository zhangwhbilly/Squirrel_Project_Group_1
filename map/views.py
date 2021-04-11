from django.shortcuts import render
from .models import Squirrel

def index(request):
    squirrel_map = Squirrel.objects.all()[:100]
    context = {
            'squirrel_map':  Squirrel.objects.all()[:100]
    }

    return render(request, 'map/index.html', context)


