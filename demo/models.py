from django.db import models


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return(self.isbn_10)


class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=36)
    description = models.TextField(blank=True, max_length=256)
    is_published = models.BooleanField(default=False)
    published = models.DateField(blank=True, null=True, default=None)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    cover = models.ImageField(blank=True, upload_to='covers/')
    number = models.OneToOneField(BookNumber, null=True, blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return(self.title)


class Character(models.Model):
    book = models.ForeignKey(
        Book, related_name='characters', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return(self.name)


class Auhtor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='auhtors')

    def __str__(self):
        return(self.surname)
