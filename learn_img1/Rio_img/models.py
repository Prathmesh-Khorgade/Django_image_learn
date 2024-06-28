from django.db import models

class ImageModel(models.Model):
    name=models.CharField(max_length=23),
    image=models.ImageField(upload_to='images')
