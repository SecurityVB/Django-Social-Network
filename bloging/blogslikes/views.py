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
        BlogsLikes.objects.get(liked_by=user, post=blog).delete()
    except:
        like = BlogsLikes.objects.create(liked_by=user, post=blog)
        like.save()

    blog.likes = BlogsLikes.objects.filter(post=blog).count()
    blog.save()


    return redirect('desk')