from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import misaka
# Create your models here.

class Blogs(models.Model):
    thumbnail_image = models.ImageField(upload_to='thumbnails',blank=False)
    title = models.CharField(max_length=300)
    slug = models.SlugField(allow_unicode=True,unique=True,editable=False)
    description = models.TextField(blank=False)
    description_html = models.TextField(editable=False,blank=False)
    author = models.CharField(max_length=250)
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' by ' + self.author

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
