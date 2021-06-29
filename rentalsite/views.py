from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rentalsite import models, forms
from rentalsite.models import Equipment, Vendor, Page, Job, OrderMaster, InvoiceDetails, ReturnSlip
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def index(request):
    return render(request, 'base.html')


def myview(request):  # login
    print('in myview')
    if request.method == "POST":
        print('in post')
        form = AuthenticationForm(request, data=request.POST)
        print(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        # form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            print('in form valid')
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("rentalsite:modules")
            else:
                return redirect("index")
        else:
            return redirect("index")
    else:
        form = AuthenticationForm()
        return render(request, template_name="base.html", context={'form': form})


# class based views
def logout_view(request):
    logout(request)
    return redirect('index')


### Testing Decorator ###
def permission_required(perm, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a particular permission
    enabled, redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """

    def check_perms(user):
        if isinstance(perm, str):
            perms = (perm,)
        else:
            perms = perm
        # First check if the user has the permission (even anon users)
        if user.has_perms(perms):
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False

    return user_passes_test(check_perms, login_url=login_url)


class ListModules(ListView):  # generic view
    template_name = 'rentalsite/list_modules_class_view.html'
    model = Equipment
    context_object_name = 'modules'


# Equipment Views

class ListDetail(DetailView):
    model = Equipment
    template_name = 'rentalsite/equipment_details.html'
    context_object_name = 'details'


class EquipmentCreate(CreateView):
    model = Equipment
    fields = ['assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned']
    template_name = 'rentalsite/equipment_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class EquipmentUpdate(UpdateView):
    model = Equipment
    fields = ['assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned']
    template_name = 'rentalsite/equipment_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class EquipmentDelete(DeleteView):
    template_name = 'rentalsite/equipment_delete.html'
    model = Equipment
    context_object_name = 'delete'
    success_url = reverse_lazy('rentalsite:modules')


# Job Views

class JobListDetail(DetailView):
    model = Job
    template_name = 'rentalsite/job_details.html'
    context_object_name = 'job_details'


class JobCreate(CreateView):
    model = Job
    fields = ['jobnum', 'ordernum', 'assetid', 'jobdetails', 'phase']
    template_name = 'rentalsite/job_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class JobUpdate(UpdateView):
    model = Job
    fields = ['jobnum', 'ordernum', 'assetid', 'jobdetails', 'phase']
    template_name = 'rentalsite/job_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class JobDelete(DeleteView):
    template_name = 'rentalsite/job_delete.html'
    model = Job
    context_object_name = 'job_delete'
    success_url = reverse_lazy('rentalsite:modules')


# Vendor Views

class VendorListDetail(DetailView):
    model = Vendor
    template_name = 'rentalsite/vendor_details.html'
    context_object_name = 'vendor_details'


class VendorCreate(CreateView):
    model = Vendor
    fields = ['vendornum', 'name', 'phonenum', 'salesman', 'ponum']
    template_name = 'rentalsite/vendor_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class VendorUpdate(UpdateView):
    model = Vendor
    fields = ['vendornum', 'name', 'phonenum', 'salesman', 'ponum']
    template_name = 'rentalsite/vendor_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class VendorDelete(DeleteView):
    template_name = 'rentalsite/vendor_delete.html'
    model = Vendor
    context_object_name = 'vendor_delete'
    success_url = reverse_lazy('rentalsite:modules')


# InvoiceDetails Views

class InvoiceListDetail(DetailView):
    model = InvoiceDetails
    template_name = 'rentalsite/invoice_details.html'
    context_object_name = 'invoice_details'


class InvoiceCreate(CreateView):
    model = InvoiceDetails
    fields = ['invoicenum', 'ordernum', 'orderdetails', 'price']
    template_name = 'rentalsite/invoice_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class InvoiceUpdate(UpdateView):
    model = InvoiceDetails
    fields = ['invoicenum', 'ordernum', 'orderdetails', 'price']
    template_name = 'rentalsite/invoice_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class InvoiceDelete(DeleteView):
    template_name = 'rentalsite/invoice_delete.html'
    model = InvoiceDetails
    context_object_name = 'invoice_delete'
    success_url = reverse_lazy('rentalsite:modules')
