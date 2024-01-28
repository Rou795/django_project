from django.urls import path

from measurement.views import SensorAPIList, SensorAPIView, MeasurementAPIAdd

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorAPIList.as_view(), name='sensor_creation'),
    path('sensors/<int:pk>/', SensorAPIView.as_view(), name='sensor_update_view'),
    path('measurements/', MeasurementAPIAdd.as_view(), name='measurements_add')
]
