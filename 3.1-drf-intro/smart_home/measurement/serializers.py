from rest_framework import serializers
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "name", "description"]


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["sensor", "temperature", "date_time"]


class OneSensSerializer(serializers.ModelSerializer):
    measurs = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ["id", "name", "description", "measurs"]
