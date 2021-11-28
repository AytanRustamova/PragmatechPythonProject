from django.shortcuts import render

def stoires(request):
    return render(request,"stories.html")