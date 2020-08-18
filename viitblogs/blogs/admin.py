from django.contrib import admin
from .models import Blogs,Comments

# from mediumeditor.admin import MediumEditorAdmin
# Register your models here.


admin.site.register(Blogs)
admin.site.register(Comments)
