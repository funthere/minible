from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

#UI-ELEMENTS
class AlertsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Alerts"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-alerts.html',greeting)

class ButtonsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Buttons"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-buttons.html',greeting)

class CardsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Cards"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-cards.html',greeting)

class CarouselView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Carousel"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-carousel.html',greeting)

class DropDownsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Dropdowns"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-dropdwons.html',greeting)

class GridView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Grid"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-grid.html',greeting)

class ImagesView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Images"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-images.html',greeting)

class LightBoxView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Lightbox"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-lightbox.html',greeting)

class ModalsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Modals"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-modals.html',greeting)

class RangeSlidebarView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Range Slider"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-rangeslidebar.html',greeting)

class OffcanvasView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Offcanvas"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-offcanvas.html',greeting)

class SessionTimeoutView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Session Timeout"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-sessiontimeout.html',greeting)

class ProgressBarsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Progress Bars"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-progressbars.html',greeting)

class PlaceholderView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Placeholder"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-placeholders.html',greeting)

class SweetAlertView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Sweet-Alert 2"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-sweetalert.html',greeting)

class TabsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Tabs & Accordions"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-tabs.html',greeting)

class TypoGraphyView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Typography"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-typography.html',greeting)

class ToastView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Toasts"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-toasts.html',greeting)

class VideoView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Video"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-video.html',greeting)

class GeneralView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "General"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-general.html',greeting)

class ColorsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Colors"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-colors.html',greeting)

class RatingView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Rating"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-rating.html',greeting)

class NotificationsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Notifications"
        greeting['heading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-notifications.html',greeting)


##FORMS
class FormelementsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Elements"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formelements.html',greeting)

class FormValidationView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Validation"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formvalidation.html',greeting)

class FormAdvancedView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Advanced"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formadvanced.html',greeting)

class FormEditorsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Editors"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formeditors.html',greeting)

class FormFileuploadView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form File Upload"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formfileupload.html',greeting)

class FormXeditableView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Xeditable"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formxeditable.html',greeting)

class FormRepeaterView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Repeater"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formrepeater.html',greeting)

class FormWizardView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Wizard"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formrwizard.html',greeting)

class FormMaskView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Mask"
        greeting['heading'] = "Forms"
        return render (request,'components/forms/forms-formrmask.html',greeting)

##Tables
class BasicTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Basic Tables"
        greeting['heading'] = "Tables"
        return render (request,'components/tables/tables-basictables.html',greeting)

class DataTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Data Tables"
        greeting['heading'] = "Tables"
        return render (request,'components/tables/tables-datatables.html',greeting)

class ResponsiveTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Responsive Table"
        greeting['heading'] = "Tables"
        return render (request,'components/tables/tables-responsivetables.html',greeting)

class EditableTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Editable Table"
        greeting['heading'] = "Tables"
        return render (request,'components/tables/tables-editabletables.html',greeting)

#Charts
class ApexChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Apex Charts"
        greeting['heading'] = "Charts"
        return render (request,'components/charts/charts-apexcharts.html',greeting)

class ChartJsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Chartjs Charts"
        greeting['heading'] = "Charts"
        return render (request,'components/charts/charts-chartjs.html',greeting)

class FlotChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Flot Charts"
        greeting['heading'] = "Charts"
        return render (request,'components/charts/charts-flotcharts.html',greeting)

class JqueryKnobChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Jquery Knob Charts"
        greeting['heading'] = "Charts"
        return render (request,'components/charts/charts-jqueryknobcharts.html',greeting)

class SparklineChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Sparkline Charts"
        greeting['heading'] = "Charts"
        return render (request,'components/charts/charts-sparklinecharts.html',greeting)

#Icons
class UnIconsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Unicons"
        greeting['heading'] = "Icons"
        return render (request,'components/icons/icons-unicons.html',greeting)

class BoxIconsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Boxicons"
        greeting['heading'] = "Icons"
        return render (request,'components/icons/icons-boxicons.html',greeting)

class MaterialDesignView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Material Design"
        greeting['heading'] = "Icons"
        return render (request,'components/icons/icons-materialdesign.html',greeting)

class DripIconsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Dripicons"
        greeting['heading'] = "Icons"
        return render (request,'components/icons/icons-dripicons.html',greeting)

class FontAwesomeView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Font Awesome"
        greeting['heading'] = "Icons"
        return render (request,'components/icons/icons-fontawesome.html',greeting)

#Maps
class GoogleMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Google Maps"
        greeting['heading'] = "Maps"
        return render (request,'components/maps/maps-googlemaps.html',greeting)

class VectorMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Vector Maps"
        greeting['heading'] = "Maps"
        return render (request,'components/maps/maps-vectormaps.html',greeting)

class LeafletMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Leaflet Maps"
        greeting['heading'] = "Maps"
        return render (request,'components/maps/maps-leafletmaps.html',greeting)