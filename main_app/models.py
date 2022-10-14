from django.db import models

# Create your models here.
class ImageModel(models.Model):
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name="Upload Time")
    last_edit_time = models.DateTimeField(auto_now=True, verbose_name="Last Edit Time")
    image_file = models.ImageField(upload_to="img/%Y%m/%d/",max_length=300, verbose_name="Image")