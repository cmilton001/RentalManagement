from django.contrib import admin
from rentalsite import models

# Register your models here.
myModels = [models.Equipment, models.Page, models.Vendor, models.Job, models.OrderMaster, models.InvoiceDetails,
            models.ReturnSlip]  # iterable list
admin.site.register(myModels)
