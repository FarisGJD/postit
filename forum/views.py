from django.shortcuts import render
from django.views import generic 
from .models import Postit


# class ThreadList(generic.ListView):
#     model = Postit
#     queryset = Postit.objects.all().order_by('-generated_on')
#     template = 'index.html'


def postit_list(request):
    postits = Postit.objects.all().order_by('-generated_on')
    context = {
        'postits': postits
    }
    return render(request, 'index.html', context)


def profile_list(request):
    postits = Postit.objects.all().order_by('-generated_on')
    context = {
        'postits': postits
    }
    return render(request, 'profile.html', context)

    
def postit_tempalte(request):
    return render(request, 'postit.html')