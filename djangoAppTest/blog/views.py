from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/templates/index.html', )

def about(request):
    return render(request, 'blog/templates/about.html')

def blog(request):
    return render(request, 'blog/templates/blogs.html')