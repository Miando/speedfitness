from django.shortcuts import render
from .models import Post

def page(request):
    posts = Post.objects.all()
    return render(request, 'blog/page.html', {'posts': posts})
