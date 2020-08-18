from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('blog_list/',views.blog_list,name="blog_list"),
    path('blog_detail/<slug:slug>/',views.blog_detail.as_view(),name="blog_detail"),

    # path('home/',views.index,name="home"),
]
