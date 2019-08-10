from django.db import models


class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=36)
    description = models.TextField(blank=True, max_length=256)
    is_published = models.BooleanField(default=False)
    published = models.DateField(blank=True, null=True, default=None)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    cover = models.ImageField(blank=True, upload_to='covers/')

    def __str__(self):
        return(self.title)
