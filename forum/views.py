from django.shortcuts import render, redirect
from .models import Postit
from django.contrib.auth.decorators import login_required


def postit_list(request):
    postits = Postit.objects.all().order_by('-generated_on')
    context = {
        'postits': postits
    }
    
    return render(request, 'index.html', context)


@login_required()
def profile_list(request):
    postits = Postit.objects.all().order_by('-generated_on')
    context = {
        'postits': postits
    }
    return render(request, 'profile.html', context)


@login_required()
def postit_tempalte(request):
    if request.method == 'POST':
        author = request.user.pk
        heading = request.POST.get('heading_name')
        body = request.POST.get('body_name')
        link = request.POST.get('url_name')
        image = request.POST.get('image_name')
        Postit.objects.create(
            slug=heading,
            author_id=author, heading=heading, body=body, link=link, image=image
            )
        return redirect('home')

    return render(request, 'postit.html')