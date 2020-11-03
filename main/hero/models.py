from django.db import models

# Create your models here.

class Plane(models.Model):
    text = models.CharField('Text', max_length=100)
    description = models.CharField('Description', max_length=100)
    price = models.IntegerField('Price')
    is_selected = models.BooleanField(default=False)

    types = [(1, "Business"), (2, "Medium"), (3, "Econome")]
    type_plane = models.IntegerField(choices=types)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return "/"
