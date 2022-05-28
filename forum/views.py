from django.shortcuts import render, redirect, get_object_or_404
from .models import Postit
from django.contrib.auth.decorators import login_required
from .forms import PostitForm


def postit_list(request):
    postits = Postit.objects.all().order_by('-generated_on')
    context = {
        'postits': postits
    }

    return render(request, 'index.html', context)


@login_required()
def create_postit(request):
    if request.method == 'POST':
        form = PostitForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = PostitForm()
    context = {
        'form': form,
    }
    return render(request, 'create-postit.html', context)


# @login_required()
# def create_postit(request):
#     if request.method == 'POST':
#         author = request.user.pk
#         heading = request.POST.get('heading_name')
#         body = request.POST.get('body_name')
#         link = request.POST.get('url_name')
#         image = request.POST.get('image_name')
#         Postit.objects.create(
#             author_id=author,
#             heading=heading,
#             body=body,
#             link=link,
#             image=image,
#             )
#         return redirect('home')
#     return render(request, 'create-postit.html')


@login_required()
def edit_postit(request, postit_id):
    postit = get_object_or_404(Postit, id=postit_id)
    if request.method == "POST":
        form = PostitForm(request.POST, instance=postit)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = PostitForm(instance=postit)
    context = {
        'form': form
    }
    return render(request, 'edit-postit.html', context)


@login_required()
def delete_postit(request, postit_id):
    postit = get_object_or_404(Postit, id=postit_id)
    postit.delete()
    return redirect('profile')


@login_required()
def profile_list(request):
    postits = Postit.objects.all().order_by('-generated_on')
    context = {
        'postits': postits
    }
    return render(request, 'profile.html', context)

