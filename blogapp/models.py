from django.db import models

# Create your models here.


from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
