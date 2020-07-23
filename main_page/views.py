from django.shortcuts import render
from .models import Post


# Create your views here.

def main_page(request):
    posts = Post.objects.all()
    return render(request, 'mainPage.html', {'posts': posts})
