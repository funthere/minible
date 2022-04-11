from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class InvoiceListView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Invoice List"
        greeting['heading'] = "Invoices"
        return render (request,'invoices/invoicelist.html',greeting)

class InvoiceDetailView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Invoice Detail"
        greeting['heading'] = "Invoices"
        return render (request,'invoices/invoicedetail.html',greeting)
