from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, OneSensSerializer, MeasurementSerializer
from django.forms import model_to_dict


class DiscrView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        post_sensor = Sensor.objects.create(
            name=request.data["name"], description=request.data["description"]
        )
        return Response({"post": model_to_dict(post_sensor)})


class OneDiscrView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = OneSensSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        update_sensor = OneSensSerializer(sensor, data=request.data)
        if update_sensor.is_valid():
            update_sensor.save()
        return Response({"patch": update_sensor.data})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        post_measurement = MeasurementSerializer(data=request.data)
        if post_measurement.is_valid(raise_exception=True):
            post_measurement.save()
        return Response({"post": post_measurement.data})
