def booked_schedule(request):
    """View to display booked appointments"""
    appointments = Appointment.objects.filter(availability='booked').order_by('appointment_date')
    context = {
        'appointments': appointments,
    }
    return render(request, 'appointment/booked_schedule.html', context)
from django.shortcuts import render, get_object_or_404
from .models import Appointment

# Create your views here.

def appointment_list(request):
    """View to display all appointments"""
    import calendar
    from datetime import date, datetime, timedelta
    from django.utils import timezone

    appointments = Appointment.objects.all().order_by('appointment_date')

    # Get month and year from GET params, fallback to current
    today = timezone.localdate()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))

    # Get all appointments for the selected month
    month_appointments = Appointment.objects.filter(
        appointment_date__year=year,
        appointment_date__month=month
    )

    # Build a dict: {day: 'booked' or 'available'}
    days_in_month = calendar.monthrange(year, month)[1]
    calendar_status = {}
    for day in range(1, days_in_month + 1):
        day_appointments = month_appointments.filter(appointment_date__day=day)
        if day_appointments.filter(availability='booked').exists():
            calendar_status[day] = 'booked'
        else:
            calendar_status[day] = 'available'

    # Build weeks for the calendar (list of lists)
    first_weekday, _ = calendar.monthrange(year, month)
    weeks = []
    week = [None] * first_weekday
    for day in range(1, days_in_month + 1):
        week.append(day)
        if len(week) == 7:
            weeks.append(week)
            week = []
    if week:
        while len(week) < 7:
            week.append(None)
        weeks.append(week)

    # For year dropdown, show a range around current year
    year_options = list(range(today.year - 2, today.year + 3))

    months = list(range(1, 13))
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    context = {
        'sierra_vista_appointment': appointments,
        'sierra_vista_appointment_count': appointments.count(),
        'calendar_status': calendar_status,
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'weeks': weeks,
        'year_options': year_options,
        'months': months,
        'month_names': month_names,
        'background_image': '/media/services/pexels-nc-farm-bureau-mark-2889440.jpg',
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
