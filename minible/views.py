from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordChangeView,PasswordSetView
from django.urls import reverse_lazy
from django.contrib.auth.models import User,auth

class DashboardView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['heading'] = "Minible"
        return render(request, 'index.html',greeting)

class CalendarView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Calendar"
        greeting['heading'] = "Minible"
        return render (request, 'calendar.html',greeting)

class ChatView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Chat"
        greeting['heading'] = "Minible"
        return render (request, 'chat.html',greeting)

class MyPasswordChangeView( PasswordChangeView):
    success_url = reverse_lazy('dashboard')

class MyPasswordSetView( PasswordSetView):
    success_url = reverse_lazy('dashboard')

def logout(request):
    auth.logout(request)
    return render(request,'account/logout.html')
