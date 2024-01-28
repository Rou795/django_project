# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerialiser, MeasurementSerializer, SensorDetailSerializer


class SensorAPIList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialiser


class SensorAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementAPIAdd(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
