from django.urls import path
from rentalsite import views

app_name = 'rentalsite'

# #URLPatterns for function based views
urlpatterns = [

#class based views urls
    path('listpages/', views.ListModules.as_view(), name='listpages'),
    path('login/', views.index, name='login'),
    #path('productdetail/<int:pk>/', views.ProductDetail.as_view(), name='productdetail'),
    #path('productnew/', views.ProductCreate.as_view(), name='productnew'),
    #path('productupdate/<int:pk>/', views.ProductUpdate.as_view(), name='productupdate'),
    #path('productdelete/<int:pk>/', views.ProductDelete.as_view(), name='productdelete'),
]