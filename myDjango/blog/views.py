from django.shortcuts import render
from .models import Post

def main_page(request):
    posts = Post.objects.all()
    return render(request, 'blog/main_page.html', {'posts': posts})