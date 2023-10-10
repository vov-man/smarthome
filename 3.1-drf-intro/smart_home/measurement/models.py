from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        "Sensor", related_name="measurs", on_delete=models.CASCADE
    )
    temperature = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)
