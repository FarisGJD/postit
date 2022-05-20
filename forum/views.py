from django.shortcuts import render
from django.views import generic 
from .models import Postit 


# class PostitList(generic.ListView):
#     model = Postit
#     template_name = 'index.html'
#     queryset = Postit.objects.filter(thread_starter=True).order_by('-created_on')
#     paginate_by = 6 
