from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.

def index(request):
    """Index view for the equipment page, showing all services/equipment"""
    services = Service.objects.all().order_by('name')
    context = {
        'equipment_list': services,
        'background_image': '/media/services/pexels-nc-farm-bureau-mark-2252618.jpg',
    }
    return render(request, 'schedule/index.html', context)

def service_list(request):
    """View to display all available services"""
    services = Service.objects.filter(availability='available').order_by('name')
    context = {
        'sierra_vista_schedule': services,
        'sierra_vista_schedule_count': services.count(),
    }
    return render(request, 'schedule/service_list.html', context)

def service_detail(request, service_id):
    """View to display individual service details"""
    service = get_object_or_404(Service, id=service_id)
    context = {
        'sierra_vista_schedule': service,
    }
    return render(request, 'schedule/service_detail.html', context)

def all_services(request):
    """View to display all services regardless of availability"""
    services = Service.objects.all().order_by('name')
    context = {
        'sierra_vista_schedule': services,
        'sierra_vista_schedule_count': services.count(),
    }
    return render(request, 'schedule/all_services.html', context)
