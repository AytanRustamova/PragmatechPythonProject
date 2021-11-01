from django.shortcuts import render
from .models import Blog

# Create your views here.


def about(request):
    return render(request, 'about.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs':blogs})