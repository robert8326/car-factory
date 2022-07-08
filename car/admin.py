from django.contrib import admin
from car import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model',)
    list_display_links = ('id', 'name', 'model',)


@admin.register(models.CarPart)
class CarPartAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'part', 'quantity',)
    list_display_links = ('id', 'car', 'part',)


@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'benefit', 'price_car', 'total_price',)
    list_display_links = ('id', 'car',)
    readonly_fields = ('total_price',)


@admin.register(models.CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


@admin.register(models.Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'percent',)
    list_display_links = ('id', 'name', 'price',)
