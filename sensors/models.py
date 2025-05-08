from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.sensor_type})"

class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.name} - {self.value} at {self.timestamp}"
