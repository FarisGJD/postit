from django.shortcuts import render
# from django.views import generic 
from .models import Postit


def home_template(request):
    return render(request, 'index.html')


def get_postit_items(request):
    items = Postit.objects.all()
    context = {
        'items': items
    }
    return render(request, 'postit.html', context)


def profile_tempalte(request):
    return render(request, 'profile.html')