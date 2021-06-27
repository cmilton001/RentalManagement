from django.urls import path
from rentalsite import views

app_name = 'rentalsite'

# #URLPatterns for function based views
urlpatterns = [

#class based views urls
    path('listpages/', views.ListModules.as_view(), name='listpages'),
    path('login/', views.index, name='login'),
    path('create/', views.EquipmentCreate.as_view(), name='create'),
    path('delete/', views.EquipmentDelete.as_view(), name='delete'),
    path('details/<int:pk>/', views.ListDetail.as_view(), name='details'),
    path('update/', views.EquipmentUpdate.as_view(), name='update')
    #path('productdetail/<int:pk>/', views.ProductDetail.as_view(), name='productdetail'),
    #path('productnew/', views.ProductCreate.as_view(), name='productnew'),
    #path('productupdate/<int:pk>/', views.ProductUpdate.as_view(), name='productupdate'),
    #path('productdelete/<int:pk>/', views.ProductDelete.as_view(), name='productdelete'),
]