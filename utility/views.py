from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class StarterPageView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Starter Page"
        greeting['heading'] = "Utility"
        return render (request,'utility/utility-starterpage.html',greeting)

class MaintainanceView(View):
    def get(self , request):
        return render (request,'utility/utility-maintainance.html')

class ComingSoonView(View):
    def get(self , request):
        return render (request,'utility/utility-comingsoon.html')

class TimeLineView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Timeline"
        greeting['heading'] = "Utility"
        return render (request,'utility/utility-timeline.html',greeting)

class FaqView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "FAQs"
        greeting['heading'] = "Utility"
        return render (request,'utility/utility-faq.html',greeting)

class PricingView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Pricing"
        greeting['heading'] = "Utility"
        return render (request,'utility/utility-pricing.html',greeting)

class ErrorPageView(View):
    def get(self , request):
        return render (request,'utility/utility-404error.html')

class ErrorPageExtraView(View):
    def get(self , request):
        return render (request,'utility/utility-500error.html')


#Authentication(Pages Only)
class AuthLoginView(View):
    def get(self , request):
        return render (request,'utility/authentication/auth-login.html')
class AuthRegisterView(View):
    def get(self , request):
        return render (request,'utility/authentication/auth-register.html')
class AuthRecoverpwView(View):
    def get(self , request):
        return render (request,'utility/authentication/auth-recoverpw.html')
class AuthLockScreenView(View):
    def get(self , request):
        return render (request,'utility/authentication/auth-lock-screen.html')