from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('blog_list/',views.blog_list,name="blog_list"),
    path('blog_detail/<slug:slug>/',views.blog_detail,name="blog_detail"),
    path('like/',views.like_post,name="like_post"),
    path('<slug:slug>/add_comment',views.add_comments,name="add_comments"),
    path('serialized/', views.blog_serialized_view, name='serialized-view')
    # path('home/',views.index,name="home"),
]
