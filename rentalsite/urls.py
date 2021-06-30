from django.urls import path
from rentalsite import views
from rentalsite.views import EquipmentSearchView

app_name = 'rentalsite'

# #URLPatterns for function based views
urlpatterns = [

    # class based views urls
    path('listpages/', views.ListModules.as_view(), name='modules'),
    ### Equipment URLS ###
    path('equipment_search/', views.EquipmentSearchView.as_view(), name='equipment_search'),
    path('details/<int:pk>/equipment_list/', views.EquipmentList.as_view(), name='equipment_list'),
    path('create/', views.EquipmentCreate.as_view(), name='create'),
    path('details/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='delete'),
    path('details/<int:pk>/', views.ListDetail.as_view(), name='details'),
    path('details/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='update'),
    ###Job URLS ###
    path('job_search/', views.JobSearchView.as_view(), name='job_search'),
    path('job_details/<int:pk>/job_list/', views.JobList.as_view(), name='job_list'),
    path('job_details/<int:pk>/', views.JobListDetail.as_view(), name='job_details'),
    path('job_create/', views.JobCreate.as_view(), name='job_create'),
    path('job_details/<int:pk>/job_update/', views.JobUpdate.as_view(), name='job_update'),
    path('job_details/<int:pk>/job_delete/', views.JobDelete.as_view(), name='job_delete'),
    ### Vendor URLS ###
    path('vendor_search/', views.VendorSearchView.as_view(), name='vendor_search'),
    path('vendor_details/<int:pk>/vendor_list/', views.VendorList.as_view(), name='vendor_list'),
    path('vendor_details/<int:pk>/', views.VendorListDetail.as_view(), name='vendor_details'),
    path('vendor_create/', views.VendorCreate.as_view(), name='vendor_create'),
    path('vendor_details/<int:pk>/vendor_update/', views.VendorUpdate.as_view(), name='vendor_update'),
    path('vendor_details/<int:pk>/vendor_delete/', views.VendorDelete.as_view(), name='vendor_delete'),
    ### InvoiceDetails URLS ###
    path('invoice_search/', views.InvoiceSearchView.as_view(), name='invoice_search'),
    path('invoice_details/<int:pk>/invoice_list/', views.InvoiceList.as_view(), name='invoice_list'),
    path('invoice_details/<int:pk>/', views.InvoiceListDetail.as_view(), name='invoice_details'),
    path('invoice_create/', views.InvoiceCreate.as_view(), name='invoice_create'),
    path('invoice_details/<int:pk>/invoice_update/', views.InvoiceUpdate.as_view(), name='invoice_update'),
    path('invoice_details/<int:pk>/invoice_delete/', views.InvoiceDelete.as_view(), name='invoice_delete'),
    ### ReturnSlip URLS ###
    path('returns_search/', views.ReturnsSearchView.as_view(), name='returns_search'),
    path('returns_details/<int:pk>/returns_list/', views.ReturnsList.as_view(), name='returns_list'),
    path('returns_details/<int:pk>/', views.ReturnsListDetail.as_view(), name='returns_details'),
    path('returns_create/', views.ReturnsCreate.as_view(), name='returns_create'),
    path('returns_details/<int:pk>/returns_update/', views.ReturnsUpdate.as_view(), name='returns_update'),
    path('returns_details/<int:pk>/returns_delete/', views.ReturnsDelete.as_view(), name='returns_delete'),
    ### Orders URLS ###
    path('order_search/', views.OrderSearchView.as_view(), name='order_search'),
    path('order_details/<int:pk>/order_list/', views.OrderList.as_view(), name='order_list'),
    path('order_details/<int:pk>/', views.OrderListDetail.as_view(), name='order_details'),
    path('order_create/', views.OrderCreate.as_view(), name='order_create'),
    path('order_details/<int:pk>/order_update/', views.OrderUpdate.as_view(), name='order_update'),
    path('order_details/<int:pk>/order_delete/', views.OrderDelete.as_view(), name='order_delete'),
    ### Reports page ###
    path('reports_list/', views.reports, name='reports_list'),
    path('category_index/', views.categories, name='category_index'),
    ### Weekly Report URLS ###
    path('weeklyreport_search/', views.WeeklyReportSearchView.as_view(), name='weeklyreport_search'),
    path('weeklyreport_details/<int:pk>/weeklyreport_list/', views.WeeklyReportList.as_view(),
         name='weeklyreport_list'),
    path('weeklyreport_details/<int:pk>/', views.WeeklyReportListDetail.as_view(), name='weeklyreport_details'),
    path('weeklyreport_create/', views.WeeklyReportCreate.as_view(), name='weeklyreport_create'),
    path('weeklyreport_details/<int:pk>/weeklyreport_update/', views.WeeklyReportUpdate.as_view(),
         name='weeklyreport_update'),
    path('weeklyreport_details/<int:pk>/weeklyreport_delete/', views.WeeklyReportDelete.as_view(),
         name='weeklyreport_delete'),
    ### Annual Rental List Report URLS ###
    path('annual_details/<int:pk>/annual_list/', views.AnnualList.as_view(), name='annual_list'),
    path('annual_details/<int:pk>/', views.AnnualListDetail.as_view(), name='annual_details'),
    path('annual_create/', views.AnnualCreate.as_view(), name='annual_create'),
    path('annual_details/<int:pk>/annual_update/', views.AnnualUpdate.as_view(), name='annual_update'),
    path('annual_details/<int:pk>/annual_delete/', views.AnnualDelete.as_view(), name='annual_delete'),
    ### Buyout Candidates Report URLS ###
    path('candidates_details/<int:pk>/candidates_list/', views.CandidateList.as_view(), name='candidates_list'),
    path('candidates_details/<int:pk>/', views.CandidateListDetail.as_view(), name='candidates_details'),
    path('candidates_create/', views.CandidateCreate.as_view(), name='candidates_create'),
    path('candidates_details/<int:pk>/candidates_update/', views.CandidateUpdate.as_view(), name='candidates_update'),
    path('candidates_details/<int:pk>/candidates_delete/', views.CandidateDelete.as_view(), name='candidates_delete'),
    ### Buyout Form List Report URLS ###
    path('buyform_details/<int:pk>/buyform_list/', views.BuyFormList.as_view(), name='buyform_list'),
    path('buyform_details/<int:pk>/', views.BuyFormListDetail.as_view(), name='buyform_details'),
    path('buyform_create/', views.BuyFormCreate.as_view(), name='buyform_create'),
    path('buyform_details/<int:pk>/buyform_update/', views.BuyFormUpdate.as_view(), name='buyform_update'),
    path('buyform_details/<int:pk>/buyform_delete/', views.BuyFormDelete.as_view(), name='buyform_delete'),
]
