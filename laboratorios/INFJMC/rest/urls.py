from django.urls import path,include
from rest_framework import routers
from . import views
from .views import CarreraviewSet

router=routers.DefaultRouter()
router.register('carrera',views.CarreraviewSet)

urlpatterns=[
path('',include(router.urls))
]