from django.db import models

# Create your models here.
from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


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


CATEGORY_CHOICES = (
    ('earthmoving', 'Earth Moving'),
    ('aerial access', 'Aerial Access'),
    ('compaction', 'Compaction'),
    ('light towers', 'Light Towers'),
)


class Category(models.Model):
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default="Earth Moving")


class Equipment(BaseModel):
    # name = models.CharField(max_length=200)
    # quantity = models.IntegerField()
    # description = models.TextField()
    # price = models.DecimalField(max_digits=4, decimal_places=2)
    # picture = models.ImageField(upload_to='images', db_column='picture', blank=True, null=True)
    assetid = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serialnum = models.CharField(max_length=200)
    vendornum = models.CharField(max_length=200)
    # category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default="Earth Moving")
    buyrent = models.CharField(max_length=4, choices=(('b', 'Buy'), ('r', 'Rent')), default='Buy')
    returned = models.CharField(max_length=1, choices=(('y', 'Y'), ('n', 'N')))

    def publish(self):
        self.save()

    def __str__(self):
        return self.assetid


class Job(models.Model):
    jobnum = models.CharField(max_length=200)
    ordernum = models.CharField(max_length=200)
    assetid = models.CharField(max_length=200)
    jobdetails = models.CharField(max_length=200)
    phase = models.CharField(max_length=200)

    def __str__(self):
        return self.jobnum


class Vendor(models.Model):
    vendornum = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phonenum = models.CharField(max_length=200)
    salesman = models.CharField(max_length=200)
    ponum = models.CharField(max_length=200)

    def __str__(self):
        return self.vendornum


class InvoiceDetails(models.Model):
    invoicenum = models.CharField(max_length=200)
    ordernum = models.CharField(max_length=200)
    orderdetails = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.invoicenum


class ReturnSlip(models.Model):
    ordernum = models.CharField(max_length=200)
    invoicenum = models.CharField(max_length=200)
    returndate = models.DateField()

    def __str__(self):
        return self.ordernum


class OrderMaster(models.Model):
    ordernum = models.CharField(max_length=200)
    jobnums = models.CharField(max_length=200)
    vendornum = models.CharField(max_length=200)
    assetnum = models.CharField(max_length=200)
    dateplaced = models.DateField()
    dateneeded = models.DateField()
    dateentered = models.DateField()
    expecteddur = models.DateField()

    def __str__(self):
        return self.ordernum


class WeeklyReport(models.Model):
    pass


class AnnualRentalList(models.Model):
    pass


class BuyoutCandidates(models.Model):
    pass


class BuyoutForm(models.Model):
    jobnum = models.CharField(max_length=200)
    vendornum = models.CharField(max_length=200)
    rentalassetid = models.CharField(max_length=200)
