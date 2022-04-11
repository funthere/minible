from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class InboxView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Inbox"
        greeting['heading'] = "Email"
        return render (request,'e_mail/e_mail-inbox.html',greeting)

class ReadEmailView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Read Email"
        greeting['heading'] = "Email"
        return render (request,'e_mail/e_mail-reademail.html',greeting)
