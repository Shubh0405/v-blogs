from django.shortcuts import render,get_object_or_404,redirect
from .models import Blogs,Comments,IP_Address
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db.models import Q

# Create your views here.
def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

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

def blog_detail(request,slug):
    blog = get_object_or_404(Blogs,slug=slug)
    comments = Comments.objects.filter(blog=blog)
    ip_address = get_ip(request)
    print('abc')
    liked = False
    try:
        u = IP_Address.objects.get(ip = ip_address)
        if u in blog.liked.all():
            print('hello')
            liked = True
    except:
        liked = False
    print(blog.liked.all())

    return render(request,'blogs/blog_detail.html',{'blog':blog,'comments':comments,'liked':liked})

def like_post(request):
    if request.method == 'POST':
        pk = request.POST.get('post_pk')
        blog = get_object_or_404(Blogs,pk = pk)
        print(blog.title)
        blog.save()
        ip_address = get_ip(request)
        try:
            u = IP_Address.objects.get(ip = ip_address)
            if u in blog.liked.all():
                blog.liked.remove(u)
            else:
                blog.liked.add(u)
        except:
            u = IP_Address(ip = ip_address)
            u.save()
            blog.liked.add(u)
        return HttpResponse()

def blog_serialized_view(request):
    data = list(Blogs.objects.values())
    return JsonResponse(data, safe=False)

def add_comments(request,slug):
    blog = get_object_or_404(Blogs,slug=slug)
    if request.method == "POST":
        try:
            writer = request.POST.get('writer')
            text = request.POST.get('text')
            obj = Comments.objects.create(blog = blog, writer=writer,text=text)
            obj.save()
            print(obj)
            return HttpResponseRedirect(reverse('blogs:blog_detail',kwargs={'slug':blog.slug}))
        except:
            message.error(request,'Something went wrong!')
            return HttpResponseRedirect(reverse('blogs:blog_detail',kwargs={'slug':blog.slug}))
