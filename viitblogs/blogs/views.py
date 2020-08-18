from django.shortcuts import render
from .models import Blogs

# Create your views here.
def index(request):
    return render(request,'blogs/index.html',{})

def blog_list(request):
    bloglist = Blogs.objects.all()
    return render(request,'blogs/blog_list.html',{'bloglist':bloglist})
