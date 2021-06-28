from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rentalsite import models
from rentalsite.models import Equipment, Vendor, Page, Job, OrderMaster, InvoiceDetails, ReturnSlip

# Create your views here.


myModels = [models.Equipment, models.Page, models.Vendor, models.Job, models.OrderMaster, models.InvoiceDetails,
            models.ReturnSlip]


def index(request):
    return render(request, 'base.html')


def myview(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
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
            return redirect("rentalsite:index")
    form = AuthenticationForm()
    return render(request, template_name="rentalsite/list_modules_class_view.html", context={'base.html': form})


# class based views

class ListModules(ListView):  # generic view
    template_name = 'rentalsite/list_modules_class_view.html'
    model = Equipment
    context_object_name = 'modules'


class ListDetail(DetailView):
    model = Equipment
    template_name = 'rentalsite/equipment_details.html'
    context_object_name = 'details'
    query_results = Equipment.objects.all()


class EquipmentCreate(CreateView):
    model = Equipment
    fields = ['assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned']
    template_name = 'rentalsite/equipment_create.html'
    success_url = reverse_lazy('rentalsite:listpages')


class EquipmentUpdate(UpdateView):
    model = Equipment
    fields = ['assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned']
    template_name = 'rentalsite/equipment_update.html'
    success_url = reverse_lazy('rentalsite:listpages')


class EquipmentDelete(DeleteView):
    template_name = 'rentalsite/equipment_delete.html'
    model = Equipment
    context_object_name = 'delete'
    success_url = reverse_lazy('rentalsite:listpages')
