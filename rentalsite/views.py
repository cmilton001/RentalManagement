from django.contrib.auth import authenticate as auth
from django.http import HttpResponseRedirect
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


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('rentalsite:listpages'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('list_modules_class_view.html')
        else:
            print('Invalid login credentials')
    return render(request, 'base.html')


# class based views

class ListModules(ListView):  # generic view
    template_name = 'rentalsite/list_modules_class_view.html'
    model = Equipment
    context_object_name = 'modules'


class ListDetail(DetailView):
    model = Equipment
    template_name = 'rentalsite/equipment_details.html'
    context_object_name = 'details'


class EquipmentCreate(CreateView):
    model = Equipment
    fields = ['assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned']
    template_name = 'rentalsite/equipment_create.html'
    success_url = reverse_lazy('rentalsite:create')


class EquipmentUpdate(UpdateView):
    model = Equipment
    fields = ['assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned']
    template_name = 'rentalsite/equipment_update.html'
    success_url = reverse_lazy('rental:update')


class EquipmentDelete(DeleteView):
    template_name = 'rentalsite/equipment_delete.html'
    model = Equipment
    context_object_name = 'delete'
    success_url = reverse_lazy('rentalsite:delete')
