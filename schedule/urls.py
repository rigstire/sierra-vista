from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.service_list, name='service_list'),
    path('services/all/', views.all_services, name='all_services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
] 