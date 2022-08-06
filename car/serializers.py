from rest_framework import serializers
from car import models as car_models


class PartSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='get_part_id')
    name = serializers.CharField(source='get_part_name')
    price = serializers.IntegerField(source='get_part_price')
    percent = serializers.IntegerField(source='get_part_percent')

    class Meta:
        model = car_models.CarPart
        fields = ('id', 'quantity', 'name', 'price', 'percent')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = car_models.Car
        fields = '__all__'


class CarPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = car_models.CarPart
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = car_models.CarModel
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    car_parts = PartSerializer(many=True)
    model = CarModelSerializer()

    class Meta:
        model = car_models.Car
        fields = ('name', 'model', 'car_parts')


class ResultSerializer(serializers.ModelSerializer):
    car = CarDetailSerializer()

    class Meta:
        model = car_models.Result
        fields = '__all__'
