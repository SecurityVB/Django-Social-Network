from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from .models import BlogsLikes
from blogs.models import Blogs
from django.contrib.auth.decorators import login_required



@login_required
def likes(request, post_id):
    user = request.user
    blog = Blogs.objects.get(pk=post_id)

    try:
        like = BlogsLikes.objects.get(liked_by=user, post=blog)
    except:
        like = None

    if like:
        like.delete()
        blog.likes -= 1
    else:
        like = BlogsLikes.objects.create(liked_by=user, post=blog)
        like.save()
        blog.likes += 1

    blog.save()

    return redirect('desk')