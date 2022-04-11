
from django.contrib import admin
from django.urls import path,include
from minible import views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

from .views import MyPasswordChangeView,MyPasswordSetView

urlpatterns = [
    path('admin/', admin.site.urls),
    #dahsboard
    path('', views.DashboardView.as_view(), name='dashboard'),
    # calendar
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    # chat
    path('chat', views.ChatView.as_view(), name='chat'),
    # Ecommerce
    path("ecommerce/", include("ecommerce.urls")),
    #Email
    path("email/",include("e_mail.urls")),
    #Invoices
    path('invoices/',include('invoices.urls')),
    #Contacts
    path('contacts/',include('contacts.urls')),
    #utility
    path('utility/',include('utility.urls')),
    #Components
    path('components/',include('components.urls')),
    # Layouts
    path('layouts/',include('layouts.urls')),
    
    path('logout',views.logout,name ='logout'),
    # Allauth
    path('account/', include('allauth.urls')),

    path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
    path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),
]
