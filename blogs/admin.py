from django.contrib import admin
from .models import Blogs,Comments,IP_Address

# from mediumeditor.admin import MediumEditorAdmin
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css: {
            "all": ("css/main.css",)
        }

        js = ("js/blog.js",)

admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comments)
admin.site.register(IP_Address)
