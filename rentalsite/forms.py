from django import forms

from rentalsite.models import Equipment, Page, Vendor, Job, InvoiceDetails, ReturnSlip, OrderMaster, Category


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned')


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('vendornum', 'name', 'phonenum', 'salesman', 'ponum')


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('name',)


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('jobnum', 'ordernum', 'assetid', 'jobdetails', 'phase')


class InvoiceDetailsForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetails
        fields = ('invoicenum', 'ordernum', 'orderdetails', 'price')


class ReturnSlipForm(forms.ModelForm):
    class Meta:
        model = ReturnSlip
        fields = ('ordernum', 'invoicenum', 'returndate')


class OrderMasterForm(forms.ModelForm):
    class Meta:
        model = OrderMaster
        fields = ('ordernum', 'jobnums', 'vendornum', 'assetid', 'dateplaced', 'dateneeded',
                  'dateentered', 'expecteddur')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('earthmoving', 'aerial access',  'compaction', 'light towers')
