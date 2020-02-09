from django.db import models

# Create your models here.
class image(models.Model):
    title=models.CharField('title', max_length=50)
    image=models.ImageField('image',upload_to='uploads/images')
    def __str__(self):
        return self.title