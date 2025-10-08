from django.db import models

# Create your models here.

class MenuFlower(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    description_detail = models.TextField(null=True,blank=True)
    price = models.FloatField()
    discount = models.FloatField()
    image = models.ImageField(null=True,blank=True,upload_to='projects/%Y/%m/%d/')
    category = models.ManyToManyField('FlowerCategory', blank=True)


    # функция которая берет название из сласса и указывает в заголовке в бд
    def __str__(self):
        return self.name


class FlowerCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

