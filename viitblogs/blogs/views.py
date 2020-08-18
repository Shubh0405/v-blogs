from django.shortcuts import render
from .models import Blogs
from django.views import generic
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)

# Create your views here.
def index(request):
    return render(request,'blogs/index.html',{})

def blog_list(request):
    bloglist = Blogs.objects.all()
    return render(request,'blogs/blog_list.html',{'bloglist':bloglist})

class blog_detail(DetailView):
    context_object_name = 'blog'
    model = Blogs
    template_name = 'blogs/blog_detail.html'

def upvote(request,slug):
    
