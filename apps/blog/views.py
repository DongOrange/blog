from django.shortcuts import get_object_or_404, redirect, render

from .form import PostForm
from .models import Post


def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
        return render(request, "blog/new.html", {"form": form})

    posts = Post.objects.order_by("-id")
    return render(request, "blog/index.html", {"posts": posts})


def new(request):
    form = PostForm()
    return render(request, "blog/new.html", {"form": form})


def edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    return render(request, "blog/edit.html", {"post": post, "form": form})


def show(req, id):
    post = get_object_or_404(Post, id=id)
    if req.method == "POST":
        form = PostForm(req.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:show", id=id)
        return render(req, "blog/edit.html", {"form": form, "post": post})
    return render(req, "blog/show.html", {"post": post})
