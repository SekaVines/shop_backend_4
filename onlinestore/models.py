from django.db import models


# Create your models here.

class Category:
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Tag:
        name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.CharField()
    category = models.ForeignKey('self', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Category, null=True, blank=True, related_name='subscription')

    def __str__(self):
        return self.title



class Review:
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(on_delete=models.CASCADE)

    def __str__(self):
        return self.text