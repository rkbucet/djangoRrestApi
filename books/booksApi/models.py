from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    published_date = models.DateTimeField()
    quantity = models.IntegerField()


def __str__(self):
    return self.title
