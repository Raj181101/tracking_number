from django.urls import path

from tracking_number_app import views

urlpatterns = [
    path('next-tracking-number/', views.ParcelTrackingView.as_view())
]