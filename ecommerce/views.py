from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ProductsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Products"
        greeting['heading'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-products.html',greeting)

class ProductDetailView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Product Detail"
        greeting['heading'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-productdetail.html',greeting)

class OrdersView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Orders"
        greeting['heading'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-orders.html',greeting)

class CustomersView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Customers"
        greeting['heading'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-customers.html',greeting)

class CartView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Cart"
        greeting['heading'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-cart.html',greeting)

class CheckOutView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Checkout"
        greeting['heading'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-checkout.html',greeting)

class ShopsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Shops"
        greeting['heading'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-shops.html',greeting)

class AddProductView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Add Product"
        greeting['heading'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-addproduct.html',greeting)

