from django.urls import path
from django.urls.conf import include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('new/', include(router.urls)),
]
