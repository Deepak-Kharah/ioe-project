from rest_framework import routers

from .api import MeasurementViewSet

router = routers.DefaultRouter()
router.register('', MeasurementViewSet, 'measurements')

urlpatterns = router.urls
