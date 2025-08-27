from django.shortcuts import render, get_object_or_404
from .models import Appointment

# Create your views here.

def appointment_list(request):
    """View to display all appointments"""
    appointments = Appointment.objects.all().order_by('appointment_date')
    context = {
        'sierra_vista_appointment': appointments,
        'sierra_vista_appointment_count': appointments.count(),
    }
    return render(request, 'appointment/appointment_list.html', context)

def available_appointments(request):
    """View to display only available appointments"""
    available_appointments = Appointment.objects.filter(availability='available').order_by('appointment_date')
    context = {
        'sierra_vista_appointment': available_appointments,
        'sierra_vista_appointment_count': available_appointments.count(),
    }
    return render(request, 'appointment/available_appointments.html', context)

def appointment_detail(request, appointment_id):
    """View to display individual appointment details"""
    appointment = get_object_or_404(Appointment, id=appointment_id)
    context = {
        'sierra_vista_appointment': appointment,
    }
    return render(request, 'appointment/appointment_detail.html', context)

def upcoming_appointments(request):
    """View to display upcoming appointments"""
    from django.utils import timezone
    upcoming = Appointment.objects.filter(
        appointment_date__gte=timezone.now()
    ).order_by('appointment_date')
    context = {
        'sierra_vista_appointment': upcoming,
        'sierra_vista_appointment_count': upcoming.count(),
    }
    return render(request, 'appointment/upcoming_appointments.html', context)
