from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=30)
    img = models.ImageField('category image', upload_to = 'media', null = True)
    about = models.TextField('category about', null = True)
    price = models.IntegerField('category price', null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class people(models.Model):
    name = models.CharField('people name', max_length=30)
    surname = models.CharField('people surname', max_length=30)
    img = models.ImageField('people image', upload_to = 'media', null = True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'people'
        verbose_name_plural = 'people'

    
