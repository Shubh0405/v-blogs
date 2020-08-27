from django.shortcuts import render,get_object_or_404,redirect
from .models import Blogs,Comments
from django.views import generic
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'blogs/index.html',{})

def blog_list(request):
    query = request.GET.get("q",None)
    bloglist = Blogs.objects.all()
    if query is not None:
        bloglist = bloglist.filter(
            Q(title__icontains=query)
        )
    return render(request,'blogs/blog_list.html',{'bloglist':bloglist})

# class blog_detail(DetailView):
#     context_object_name = 'blog'
#     model = Blogs
#     template_name = 'blogs/blog_detail.html'

def blog_detail(request,slug):
    blog = get_object_or_404(Blogs,slug=slug)
    comments = Comments.objects.filter(blog=blog)
    return render(request,'blogs/blog_detail.html',{'blog':blog,'comments':comments})

def upvote(request,slug):
    blog = get_object_or_404(Blogs,slug=slug)
    blog.upvotes += 1
    blog.save()
    return HttpResponseRedirect(reverse('blogs:blog_detail',kwargs={'slug':blog.slug}))

def add_comments(request,slug):
    blog = get_object_or_404(Blogs,slug=slug)
    if request.method == "POST":
        try:
            writer = request.POST.get('writer')
            text = request.POST.get('text')
            obj = Comments.objects.create(blog = blog, writer=writer,text=text)
            obj.save()
            return HttpResponseRedirect(reverse('blogs:blog_detail',kwargs={'slug':blog.slug}))
        except:
            message.error(request,'Something went wrong!')
            return HttpResponseRedirect(reverse('blogs:blog_detail',kwargs={'slug':blog.slug}))
