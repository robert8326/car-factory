from rest_framework import generics
from rest_framework import viewsets
from car import models as car_models
from car import serializers as car_serializer
from rest_framework.pagination import LimitOffsetPagination


class CarAPIViewSet(viewsets.ModelViewSet):
    queryset = car_models.Car.objects.all()
    serializer_class = car_serializer.CarSerializer
    pagination_class = LimitOffsetPagination
    http_method_names = ('post', 'put', 'delete', 'get')


class CarPartAPIViewSet(viewsets.ModelViewSet):
    queryset = car_models.CarPart.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = car_serializer.CarPartSerializer
    http_method_names = ('post', 'put', 'delete', 'get')


class CarModelAPIViewSet(viewsets.ModelViewSet):
    queryset = car_models.CarModel.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = car_serializer.CarModelSerializer
    http_method_names = ('post', 'put', 'delete', 'get')


class ResultListAPIView(generics.ListAPIView):
    queryset = car_models.Result.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = car_serializer.ResultSerializer


class ResultRetrieveAPIView(generics.RetrieveAPIView):
    queryset = car_models.Result.objects.all()
    serializer_class = car_serializer.ResultSerializer
