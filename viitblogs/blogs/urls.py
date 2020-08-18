from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('blog_list/',views.blog_list,name="blog_list"),
    
    # path('home/',views.index,name="home"),
]
