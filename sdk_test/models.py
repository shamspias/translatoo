from django.db import models


# Create your models here.

class MyImage(models.Model):
    """
    Showing Image
    """
    image = models.ImageField(default='avatar.png', upload_to='images/')

    def __str__(self):
        return "Images"
