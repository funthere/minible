from django.urls import path
from e_mail import views

urlpatterns = [
    #email
    path('inbox',views.InboxView.as_view(),name='email-inbox'),
    path('reademail',views.ReadEmailView.as_view(),name='email-reademail'),
]    