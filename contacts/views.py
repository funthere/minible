from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class UserGridView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "User Grid"
        greeting['heading'] = "Contacts"
        return render (request,'contacts/contacts-usergrid.html',greeting)

class UserListView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "User List"
        greeting['heading'] = "Contacts"
        return render (request,'contacts/contacts-userlist.html',greeting)

class ProfileView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Profile"
        greeting['heading'] = "Contacts"
        return render (request,'contacts/contact-profile.html',greeting)