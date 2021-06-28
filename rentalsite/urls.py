from django.urls import path
from rentalsite import views

app_name = 'rentalsite'

# #URLPatterns for function based views
urlpatterns = [

#class based views urls
    path('listpages/', views.ListModules.as_view(), name='listpages'),
    path('login/', views.index, name='login'),
    path('create/', views.EquipmentCreate.as_view(), name='create'),
    path('details/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='delete'),
    path('details/<int:pk>/', views.ListDetail.as_view(), name='details'),
    path('details/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='update'),
]
