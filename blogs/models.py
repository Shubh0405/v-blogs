from django.db import models
from django.utils.text import slugify
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
import misaka
# Create your models here.

class IP_Address(models.Model):
    ip = models.TextField(default=None)

    def __str__(self):
        return self.ip


class Blogs(models.Model):
    thumbnail_image = models.ImageField(upload_to='thumbnails',blank=False)
    title = models.CharField(max_length=300)
    slug = models.SlugField(allow_unicode=True,unique=True,editable=False)
    description = models.TextField(blank=False)
    description_html = models.TextField(editable=False,blank=False)
    author = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(IP_Address, blank=True, editable=False)

    def __str__(self):
        return self.title + ' by ' + self.author

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('blogs:blog_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']

class Comments(models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE, related_name = 'comments')
    writer = models.CharField(max_length=150)
    text = models.TextField(blank=False)
    text_html = models.TextField(editable=False,blank=False)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.blog.title + ' --> ' + self.writer

    def save(self,*args,**kwargs):
        self.text_html = misaka.html(self.text)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
