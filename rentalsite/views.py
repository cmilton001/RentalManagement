from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from rentalsite.models import Equipment, Vendor, Page, Job, OrderMaster, InvoiceDetails, ReturnSlip, WeeklyReport, \
    AnnualRentalList, BuyoutCandidates, BuyoutForm
from django.contrib.auth.decorators import login_required, user_passes_test
from rentalsite.mixin import GroupRequiredMixin
from django.views.generic import View


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


class ListModules(TemplateView):  # generic view
    template_name = 'rentalsite/list_modules_class_view.html'
    model = Equipment
    context_object_name = 'modules'


def reports(request):
    return render(request, 'rentalsite/reports_list.html')


# Equipment Views
class EquipmentList(ListView):  # generic view
    template_name = 'rentalsite/equipment_list.html'
    model = Equipment
    context_object_name = 'equipment_list'


class ListDetail(DetailView):
    model = Equipment
    template_name = 'rentalsite/equipment_details.html'
    context_object_name = 'details'


class EquipmentSearchView(ListView):
    model = Equipment
    template_name = 'rentalsite/equipment_search.html'
    context_object_name = 'equipment_search'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Equipment.objects.filter(
            Q(make__icontains=query) | Q(model__icontains=query) | Q(assetid__icontains=query) |
            Q(serialnum__icontains=query) | Q(vendornum__icontains=query) | Q(category__icontains=query)
            | Q(buyrent__icontains=query) | Q(returned__icontains=query)
        )
        return object_list


class EquipmentCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = Equipment
    fields = ['assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned']
    template_name = 'rentalsite/equipment_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class EquipmentUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = Equipment
    fields = ['assetid', 'make', 'model', 'serialnum', 'vendornum', 'category', 'buyrent', 'returned']
    template_name = 'rentalsite/equipment_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class EquipmentDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/equipment_delete.html'
    model = Equipment
    context_object_name = 'delete'
    success_url = reverse_lazy('rentalsite:modules')


# Job Views

class JobList(ListView):  # generic view
    template_name = 'rentalsite/job_list.html'
    model = Job
    context_object_name = 'job_list'


class JobListDetail(DetailView):
    model = Job
    template_name = 'rentalsite/job_details.html'
    context_object_name = 'job_details'


class JobCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = Job
    fields = ['jobnum', 'ordernum', 'assetid', 'jobdetails', 'phase']
    template_name = 'rentalsite/job_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class JobUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = Job
    fields = ['jobnum', 'ordernum', 'assetid', 'jobdetails', 'phase']
    template_name = 'rentalsite/job_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class JobDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/job_delete.html'
    model = Job
    context_object_name = 'job_delete'
    success_url = reverse_lazy('rentalsite:modules')


# Vendor Views

class VendorList(ListView):  # generic view
    template_name = 'rentalsite/vendor_list.html'
    model = Vendor
    context_object_name = 'vendor_list'


class VendorListDetail(DetailView):
    model = Vendor
    template_name = 'rentalsite/vendor_details.html'
    context_object_name = 'vendor_details'


class VendorCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = Vendor
    fields = ['vendornum', 'name', 'phonenum', 'salesman', 'ponum']
    template_name = 'rentalsite/vendor_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class VendorUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = Vendor
    fields = ['vendornum', 'name', 'phonenum', 'salesman', 'ponum']
    template_name = 'rentalsite/vendor_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class VendorDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/vendor_delete.html'
    model = Vendor
    context_object_name = 'vendor_delete'
    success_url = reverse_lazy('rentalsite:modules')


# InvoiceDetails Views

class InvoiceList(ListView):  # generic view
    template_name = 'rentalsite/invoice_list.html'
    model = InvoiceDetails
    context_object_name = 'invoice_list'


class InvoiceListDetail(DetailView):
    model = InvoiceDetails
    template_name = 'rentalsite/invoice_details.html'
    context_object_name = 'invoice_details'


class InvoiceCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = InvoiceDetails
    fields = ['invoicenum', 'ordernum', 'orderdetails', 'price']
    template_name = 'rentalsite/invoice_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class InvoiceUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = InvoiceDetails
    fields = ['invoicenum', 'ordernum', 'orderdetails', 'price']
    template_name = 'rentalsite/invoice_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class InvoiceDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/invoice_delete.html'
    model = InvoiceDetails
    context_object_name = 'invoice_delete'
    success_url = reverse_lazy('rentalsite:modules')


# Return Slip Views

class ReturnsList(ListView):  # generic view
    template_name = 'rentalsite/returns_list.html'
    model = ReturnSlip
    context_object_name = 'returns_list'


class ReturnsListDetail(DetailView):
    model = ReturnSlip
    template_name = 'rentalsite/returns_details.html'
    context_object_name = 'returns_details'


class ReturnsCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = ReturnSlip
    fields = ['ordernum', 'invoicenum', 'returndate']
    template_name = 'rentalsite/returns_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class ReturnsUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = ReturnSlip
    fields = ['ordernum', 'invoicenum', 'returndate']
    template_name = 'rentalsite/returns_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class ReturnsDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/returns_delete.html'
    model = ReturnSlip
    context_object_name = 'returns_delete'
    success_url = reverse_lazy('rentalsite:modules')


# Order Views

class OrderList(ListView):  # generic view
    template_name = 'rentalsite/order_list.html'
    model = OrderMaster
    context_object_name = 'order_list'


class OrderListDetail(DetailView):
    model = OrderMaster
    template_name = 'rentalsite/order_details.html'
    context_object_name = 'order_details'


class OrderCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = OrderMaster
    fields = ['ordernum', 'jobnums', 'vendornum', 'assetid', 'dateplaced', 'dateneeded', 'dateentered', 'expecteddur']
    template_name = 'rentalsite/order_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class OrderUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = OrderMaster
    fields = ['ordernum', 'jobnums', 'vendornum', 'assetid', 'dateplaced', 'dateneeded', 'dateentered', 'expecteddur']
    template_name = 'rentalsite/order_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class OrderDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/order_delete.html'
    model = OrderMaster
    context_object_name = 'order_delete'
    success_url = reverse_lazy('rentalsite:modules')


# Weekly Report Views

class WeeklyReportList(ListView):  # generic view
    template_name = 'rentalsite/weeklyreport_list.html'
    model = OrderMaster
    context_object_name = 'weeklyreport_list'


class WeeklyReportListDetail(DetailView):
    model = WeeklyReport
    template_name = 'rentalsite/weeklyreport_details.html'
    context_object_name = 'weeklyreport_details'


class WeeklyReportCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = WeeklyReport
    fields = ['buyrent', 'jobnum', 'activejob', 'vendornum', 'returned', 'datereceived', 'datereturned',
              'rentaldatefrom', 'rentaldateto', ]
    template_name = 'rentalsite/weeklyreport_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class WeeklyReportUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = WeeklyReport
    fields = ['buyrent', 'jobnum', 'activejob', 'vendornum', 'returned', 'datereceived', 'datereturned',
              'rentaldatefrom', 'rentaldateto', ]
    template_name = 'rentalsite/weeklyreport_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class WeeklyReportDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/weeklyreport_delete.html'
    model = WeeklyReport
    context_object_name = 'weeklyreport_delete'
    success_url = reverse_lazy('rentalsite:modules')


# Annual Rental List Views
class AnnualList(ListView):
    template_name = 'rentalsite/annual_list.html'
    model = AnnualRentalList
    context_object_name = 'annual_list'


class AnnualListDetail(DetailView):
    model = AnnualRentalList
    template_name = 'rentalsite/annual_details.html'
    context_object_name = 'annual_details'


class AnnualCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = AnnualRentalList
    fields = ['buyrent', 'jobnum', 'vendornum', 'returned', 'buyoutprice', 'todaterentals']
    template_name = 'rentalsite/annual_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class AnnualUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = AnnualRentalList
    fields = ['buyrent', 'jobnum', 'vendornum', 'returned', 'buyoutprice', 'todaterentals']
    template_name = 'rentalsite/annual_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class AnnualDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/annual_delete.html'
    model = AnnualRentalList
    context_object_name = 'annual_delete'
    success_url = reverse_lazy('rentalsite:modules')


# Buy-out Candidate Views
class CandidateList(ListView):
    template_name = 'rentalsite/candidates_list.html'
    model = BuyoutCandidates
    context_object_name = 'candidates_list'


class CandidateListDetail(DetailView):
    model = BuyoutCandidates
    template_name = 'rentalsite/candidates_details.html'
    context_object_name = 'candidates_details'


class CandidateCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = BuyoutCandidates
    fields = ['buyrent', 'jobnum', 'vendornum', 'returned', 'buyoutprice', 'todaterentals']
    template_name = 'rentalsite/candidates_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class CandidateUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = BuyoutCandidates
    fields = ['buyrent', 'jobnum', 'vendornum', 'returned', 'buyoutprice', 'todaterentals']
    template_name = 'rentalsite/candidates_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class CandidateDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/candidates_delete.html'
    model = BuyoutCandidates
    context_object_name = 'candidates_delete'
    success_url = reverse_lazy('rentalsite:modules')


# Buy-out Form Views
class BuyFormList(ListView):
    template_name = 'rentalsite/buyform_list.html'
    model = BuyoutForm
    context_object_name = 'buyform_list'


class BuyFormListDetail(DetailView):
    model = BuyoutForm
    template_name = 'rentalsite/buyform_details.html'
    context_object_name = 'buyform_details'


class BuyFormCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    model = BuyoutForm
    fields = ['jobnum', 'vendornum', 'rentalassetid']
    template_name = 'rentalsite/buyform_create.html'
    success_url = reverse_lazy('rentalsite:modules')


class BuyFormUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    model = BuyoutForm
    fields = ['jobnum', 'vendornum', 'rentalassetid']
    template_name = 'rentalsite/buyform_update.html'
    success_url = reverse_lazy('rentalsite:modules')


class BuyFormDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    template_name = 'rentalsite/buyform_delete.html'
    model = BuyoutForm
    context_object_name = 'buyform_delete'
    success_url = reverse_lazy('rentalsite:modules')

