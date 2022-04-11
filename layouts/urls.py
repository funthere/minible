from django.urls import path
from layouts import views
urlpatterns = [
    # Vertical Layout
    path('dark-Sidebar',views.DarkSidebarView.as_view(),name='dark_sidebar'),
    path('compact-Sidebar',views.CompactSidebarView.as_view(),name='compact_sidebar'),
    path('icon-Sidebar',views.IconSidebarView.as_view(),name='icon_sidebar'),
    path('boxed-Width-Sidebar',views.BoxWidthSidebarView.as_view(),name='boxed_width_sidebar'),
    path('preloader-Sidebar',views.PreloaderSidebarView.as_view(),name='preloader_sidebar'),
    path('colored-Sidebar',views.ColoredSidebarView.as_view(),name='colored_sidebar'),
    
    #Horizontal Layout
    path('horizontal',views.HorizontalView.as_view(),name='horizontal'),
    path('Horizontal-dark-Topbar',views.DarkTopbarHoriView.as_view(),name='hori_topbar_dark'),
    path('Horizontal-Boxed-Width',views.BoxedWidthHoriView.as_view(),name='hori_boxed_width'),
    path('Horizontal-Preloader',views.PreloaderHoriView.as_view(),name='hori_preloader'),
]    