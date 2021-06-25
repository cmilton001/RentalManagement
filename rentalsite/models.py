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
        return Equipment.objects.filter(page__name=self.name)


class Equipment(models.Model):
    # name = models.CharField(max_length=200)
    # quantity = models.IntegerField()
    # description = models.TextField()
    # price = models.DecimalField(max_digits=4, decimal_places=2)
    # picture = models.ImageField(upload_to='images', db_column='picture', blank=True, null=True)
    assetid = make = model = serialnum = vendornum = models.CharField(max_length=200)
    category = models.ForeignKey(Page, null=False, on_delete=models.CASCADE)
    buyrent = models.CharField(max_length=4, choices=['Buy', 'Rent'], default='Buy')
    returned = models.CharField(max_length=1, choices=['Y', 'N'])

    class Meta:
        ordering = ['name']

    def publish(self):
        self.save()


class Job(models.Model):
    jobnum = ordernum = assetid = jobdetails = phase = models.CharField(max_length=200)


class Vendor(models.Model):
    vendornum = name = phonenum = salesman = ponum = models.CharField(max_length=200)


class InvoiceDetails(models.Model):
    invoicenum = ordernum = orderdetails = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ReturnSlip(models.Model):
    ordernum = invoicenum = returndate = models.CharField(max_length=200)


class OrderMaster(models.Model):
    ordernum = jobnums = vendornum = assetnum = dateplaced = dateneeded = dateentered = expecteddur = models.CharField(max_length=200)

