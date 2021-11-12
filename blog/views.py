from django.shortcuts import render
from blog.forms import CommentForm
from blog.models import Category, Post, Comment
# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # This code creates a commments form
    form = CommentForm()
    # check and validate form on submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            # save comment
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)
