from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='projects/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title