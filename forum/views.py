from django.shortcuts import render
from django.views import generic 
from .models import Postit 


# class PostitList(generic.ListView):
#     model = Postit
#     template_name = 'base.html'
#     queryset = Postit.objects.filter(thread_starter=True).order_by('-generated_on')
#     paginate_by = 6

def base_template(request):
    return render(request, 'base.html')

