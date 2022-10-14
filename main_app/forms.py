from django import forms
from main_app import models

class ImageModelForm(forms.ModelForm):
    image_file = forms.FileField(label="Click Me Select Image!")
    class Meta:
        model = models.ImageModel
        fields = ("image_file", )