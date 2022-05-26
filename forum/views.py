from django.shortcuts import render, redirect
# from django.views import generic 
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


# def full_thread(request, slug):
#     thread = Postit.objects.all()
#     post = get_object_or_404(thread, slug=slug)
#     comments = post.comments.filter(approved=True).order_by('created_on')
#     upvote = False
#     if post.votes.filter(id=request.user.id).exists():
#         upvote = True
        
#         return render(request, 'full-thread.html', {
#             "post": post, 
#             "comments": comments,
#             "upvote": upvote
#         },
#         )


def profile_list(request):
    postits = Postit.objects.all().order_by('-generated_on')
    context = {
        'postits': postits
    }
    return render(request, 'profile.html', context)


def postit_tempalte(request):
    if request.method == 'POST':
        heading = request.POST.get('heading_name')
        body = request.POST.get('body_name')
        link = request.POST.get('url_name')
        image = request.POST.get('image_name')
        Postit.objects.create(
            heading=heading, body=body, link=link, image=image
            )
        return redirect('home')

    return render(request, 'postit.html')