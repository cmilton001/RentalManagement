from django.db import models

# Create your models here.
from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_pages(self):
        return Product.objects.filter(page__name=self.name)


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    # category = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    #picture = models.ImageField(null=False)  # where to upload??
    #picture = models.ImageField(max_length=255, null=True, blank=True, upload_to='images/%Y/%m/%d')
    picture = models.ImageField(upload_to='images', db_column='picture', blank=True, null=True)
    category = models.ForeignKey(Page, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
