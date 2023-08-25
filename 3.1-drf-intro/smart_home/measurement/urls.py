from django.contrib import admin
from django.urls import path
from measurement.views import DiscrView, MeasurementView,OneDiscrView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', DiscrView.as_view()),
    path('sensors/<pk>/', OneDiscrView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
