from django import template
from ..models import Blogs

register = template.Library()

@register.inclusion_tag("blogs/desk.html")
def show_posts():
    posts = Blogs.objects.all()
    return {"posts": posts}