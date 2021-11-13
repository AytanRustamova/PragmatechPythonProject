# Blog Views
from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.


def about(request):
    return render(request, 'about.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs':blogs})

def blog_detail(request, slug):
    blogs = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog-details.html', {'blogs': blogs})