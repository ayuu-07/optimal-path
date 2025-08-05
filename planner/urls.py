from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plan/', views.plan_trip, name='plan_trip'),
    path('view/<int:trip_id>/', views.view_itinerary, name='view_itinerary'),
    path('download/<int:trip_id>/', views.download_pdf, name='download_pdf'),
]
