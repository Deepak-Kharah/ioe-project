from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Measurement
from .serializers import MeasurementSerializer


class MeasurementViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
