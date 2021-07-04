from django.db import models


class Picture(models.Model):
    path = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f'{type(self).__name__} with path {self.path}'
