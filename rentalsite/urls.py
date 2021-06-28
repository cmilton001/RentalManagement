from django.urls import path
from rentalsite import views

app_name = 'rentalsite'

# #URLPatterns for function based views
urlpatterns = [

    # class based views urls
    path('listpages/', views.ListModules.as_view(), name='modules'),
    path('create/', views.EquipmentCreate.as_view(), name='create'),
    path('details/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='delete'),
    path('details/<int:pk>/', views.ListDetail.as_view(), name='details'),
    path('details/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='update'),
    ###Job URLS ###
    path('job_details/<int:pk>/', views.JobListDetail.as_view(), name='job_details'),
    path('job_create/', views.JobCreate.as_view(), name='job_create'),
    path('job_details/<int:pk>/job_update/', views.JobUpdate.as_view(), name='job_update'),
    path('job_details/<int:pk>/job_delete/', views.JobDelete.as_view(), name='job_delete'),
]
