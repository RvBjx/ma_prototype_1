from django.shortcuts import render
from .models import Sensor, SensorReading

def dashboard(request):
    sensors = Sensor.objects.all()
    readings = SensorReading.objects.order_by('-timestamp')[:50]
    return render(request, 'sensors/dashboard.html', {'sensors': sensors, 'readings': readings})
