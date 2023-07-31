from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
path('about/',views.aboutus, name="aboutUs"),
path('contact/',views.contactus, name="contactUs"),
path('tracker/',views.tracker, name="tracker"),
path('search/',views.search, name="search"),
path('productview/', views.productview, name='productview'),
path('billing_address/', views.billing_address, name='billing_address'),
path('final_checkout/', views.final_checkout, name='final_checkout'),
path('product/<int:product_id>/', views.product_detail, name='product_detail'),
path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
path('checkout/', views.checkout, name='checkout'),
path('some_view/', views.some_view, name='some_view'),
path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
path('process_order/', views.process_order, name='process_order'),

]