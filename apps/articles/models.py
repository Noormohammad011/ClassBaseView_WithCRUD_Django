from django.db import models
from DjangoClass.utils import get_unique_slug




class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, null=True, unique=True)
    body = models.TextField(max_length=500)
    is_public = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField(max_length=677)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    
   
