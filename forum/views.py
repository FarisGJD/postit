from django.shortcuts import render
from django.views import generic 
from .models import Postit


def base_template(request):
    return render(request, 'base.html')


def get_postit_items(request):
    items = Postit.objects.all()
    context = {
        'items': items
    }
    return render(request, 'create-postit.html', context)
