from django.urls import include, path
from . import views

urlpatterns = [
    path('circuits/', views.CircuitListView.as_view(), name='circuit-list'),
    path('circuit/<int:circuitId>/', views.CircuitDetailView.as_view(), name='circuit-detail'),
    path('races/year/<int:year>/', views.RaceListByYearView.as_view(), name='race-list-by-year'),
    path('drivers/', views.DriverListView.as_view(), name='driver-list'),
    path('driver/summary/<int:driverId>/', views.DriverSummaryView.as_view(), name='driver-summary'),
    path('driver/add/', views.DriverCreateView.as_view(), name='driver-add'),
    path('driver/update/<int:driverId>/', views.DriverUpdateView.as_view(), name='driver-update'),
    path('driver/delete/<int:driverId>/', views.DriverDeleteView.as_view(), name='driver-delete'),
]