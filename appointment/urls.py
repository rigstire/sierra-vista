from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('available/', views.available_appointments, name='available_appointments'),
    path('upcoming/', views.upcoming_appointments, name='upcoming_appointments'),
    path('booked-schedule/', views.booked_schedule, name='booked_schedule'),
    path('<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
] 