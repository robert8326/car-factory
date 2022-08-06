from django.urls import path
from rest_framework import routers
from car import views as car_views

router = routers.DefaultRouter()
router.register('car', car_views.CarAPIViewSet, basename='cars')
router.register('car_model', car_views.CarModelAPIViewSet, basename='cars model')
router.register('car_part', car_views.CarPartAPIViewSet, basename='cars part')

urlpatterns = [
    path('result/', car_views.ResultListAPIView.as_view()),
    path('result/<int:pk>', car_views.ResultRetrieveAPIView.as_view()),
]

urlpatterns += router.urls
