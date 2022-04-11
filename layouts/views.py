from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# Vertical

class DarkSidebarView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Dark Sidebar"
        greeting['heading'] = "Layouts"
        return render (request,'layouts/vertical/layouts-dark-sidebar.html',greeting)

class CompactSidebarView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Compact Sidebar"
        greeting['heading'] = "Layouts"
        return render (request,'layouts/vertical/layouts-compact-sidebar.html',greeting)

class IconSidebarView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Icon Sidebar"
        greeting['heading'] = "Layouts"
        return render (request,'layouts/vertical/layouts-icon-sidebar.html',greeting)

class BoxWidthSidebarView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Boxed Width"
        greeting['heading'] = "Layouts"
        return render (request,'layouts/vertical/layouts-boxed-width-sidebar.html',greeting)

class PreloaderSidebarView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Preloader "
        greeting['heading'] = "Layouts"
        return render (request,'layouts/vertical/layouts-preloader-sidebar.html',greeting)

class ColoredSidebarView(View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Colored Sidebar"
        greeting['heading'] = "Layouts"
        return render (request,'layouts/vertical/layouts-colored-sidebar.html',greeting)

# Horizontal

class HorizontalView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "Horizontal "
        greeting['heading'] = "Layouts"
        return render (request,'layouts/horizontal/layouts-horizontal.html',greeting)

class DarkTopbarHoriView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "Topbar Dark"
        greeting['heading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-hori-topbar-dark.html',greeting)

class BoxedWidthHoriView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "Boxed Width"
        greeting['heading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-hori-boxed-width.html',greeting)

class PreloaderHoriView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "Preloader"
        greeting['heading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-hori-preloader.html',greeting)