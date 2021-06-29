from django.contrib import admin
from django.contrib.auth.models import Group

from rentalsite import models

# Register your models here.
myModels = [models.Equipment, models.Page, models.Vendor, models.Job, models.OrderMaster, models.InvoiceDetails,
            models.ReturnSlip, models.WeeklyReport, models.AnnualRentalList, models.BuyoutForm, models.BuyoutCandidates
            ]  # iterable list
admin.site.register(myModels)

''''
class Admin(Group):
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


class Viewer(Group):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_module_permission(self, request):
        return False

    def has_view_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return False
'''''