from django.shortcuts import render, redirect, get_object_or_404
from .models import Postit
from django.contrib.auth.decorators import login_required
from .forms import PostitForm, PostitComments
from django.views import View


def postit_list(request):
    postits = Postit.objects.all().order_by("-generated_on")
    context = {
        "postits": postits,
    }

    return render(request, "index.html", context)


class FullThread(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Postit.objects.all()
        postit = get_object_or_404(queryset, slug=slug)
        comments = postit.comments.filter(approved=True).order_by(
            "date_created")
        return render(
            request,
            "full-thread.html",
            {
                "postit": postit,
                "comments": comments,
                "commented": False,
                "postit_comments": PostitComments(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Postit.objects.all()
        postit = get_object_or_404(queryset, slug=slug)
        comments = postit.comments.filter(approved=True).order_by(
            "date_created")

        postit_comments = PostitComments(data=request.POST)

        if postit_comments.is_valid():
            postit_comments.instance.email = request.user.email
            postit_comments.instance.name = request.user.username
            comment = postit_comments.save(commit=False)
            comment.postit = postit
            comment.username = request.user
            comment.save()

        else:
            postit_comments = PostitComments()

        return render(
            request,
            "full-thread.html",
            {
                "postit": postit,
                "comments": comments,
                "commented": True,
                "postit_comments": PostitComments(),
            },
        )


@login_required()
def create_postit(request):
    if request.method == "POST":
        form = PostitForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
        return redirect("home")
    form = PostitForm()
    context = {
        "form": form,
    }
    return render(request, "create-postit.html", context)


@login_required()
def edit_postit(request, postit_id):
    postit = get_object_or_404(Postit, id=postit_id)
    if request.method == "POST":
        form = PostitForm(request.POST, instance=postit)
        if form.is_valid():
            form.save()
            return redirect("profile")
    form = PostitForm(instance=postit)
    context = {"form": form}
    return render(request, "edit-postit.html", context)


@login_required()
def delete_postit(request, postit_id):
    postit = get_object_or_404(Postit, id=postit_id)
    postit.delete()
    return redirect("profile")


@login_required()
def profile_list(request):
    postits = Postit.objects.filter(author=request.user).order_by(
        "-generated_on"
        )
    context = {
        "postits": postits,
    }
    return render(request, "profile.html", context)
