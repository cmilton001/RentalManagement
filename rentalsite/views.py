from django.contrib.auth import authenticate, login
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
    if request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        #if not (user.is_authenticated()):
          #  return redirect('login.html')

        if user is not None:
            login(request, user)
            return redirect('success.html')
        else:
            render(request, 'login.html')



    return render(request, 'login.html')


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
