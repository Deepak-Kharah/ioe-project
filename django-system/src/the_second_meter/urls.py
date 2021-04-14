from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('user/', include('user.urls')),
    path('dashboard/', include('arduino.urls')),
    path('api/measure', include('tsm_api.urls'))
]
