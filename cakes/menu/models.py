from django.db import models

# Create your models here.

class MenuCake(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField()
    image = models.ImageField(null=True,blank=True,upload_to='projects/%Y/%m/%d/')

    # функция которая берет название из сласса и указывает в заголовке в бд
    def __str__(self):
        return self.name