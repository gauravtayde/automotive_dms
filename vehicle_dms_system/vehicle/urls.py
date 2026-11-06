from django.urls import path
from vehicle import views

urlpatterns = [
    path('vehicle/', views.vehicle_list, name='vehicle_list'),
    path('vehicle/create', views.create_vehicle, name='create'),
    path('vehicle/<int:pk>/update', views.update_vehicle, name='update'),
    path('vehicle/<int:pk>/get', views.get_vehicle, name='update'),
    path('vehicle/<int:pk>/delete', views.delete_vehicle, name='delete'),
    path('cbv/vehicle/', views.VehicleListCreateView.as_view(),
         name='cbv_vehicle_list')
]
