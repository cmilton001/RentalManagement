from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rentalsite import models, forms
from rentalsite.models import Equipment, Vendor, Page, Job, OrderMaster, InvoiceDetails, ReturnSlip, Admin


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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("rentalsite:modules")
            else:
                return redirect("rentalsite:index")
        else:
            return redirect("index")
    else:
        form = AuthenticationForm()
        return render(request, template_name="base.html", context={'form': form})


# class based views
def logout_view(request):
    logout(request)
    return redirect('index')


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
