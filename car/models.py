from django.db import models
from django.db.models import F, Sum


class Part(models.Model):
    """ Части машины """
    name = models.CharField(max_length=155, verbose_name='Название', unique=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    percent = models.PositiveSmallIntegerField(verbose_name='Процент', help_text='Процент производителя на товар')

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """ Модели машин """
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'CarModel'
        verbose_name_plural = 'CarModel'

    def __str__(self):
        return self.name


class Car(models.Model):
    """ Машины """
    name = models.CharField(max_length=155, verbose_name='Название')
    model = models.ForeignKey('CarModel', verbose_name='Модель', related_name='cars', on_delete=models.CASCADE)
    parts = models.ManyToManyField('Part', through='CarPart', related_name='cars', verbose_name='детали')

    @property
    def total_price(self):
        return self.parts.aggregate(
            total=Sum(
                ((F('price') * F('percent') / 100) + F('price')) * F('car_parts__quantity')
            )
        )['total']

    @property
    def price_car(self):
        return self.parts.aggregate(
            total=Sum(
                F('price') * F('car_parts__quantity')
            )
        )['total']

    @property
    def benefit(self):
        return self.total_price - self.price_car


class CarPart(models.Model):
    """ Для добавления количества запчасти """
    part = models.ForeignKey('Part', verbose_name='Деталь', related_name='car_parts', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', verbose_name='Машина', related_name='car_parts', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количества детали')

    def get_part_id(self):
        return self.part.id

    def get_part_name(self):
        return self.part.name

    def get_part_price(self):
        return self.part.price

    def get_part_percent(self):
        return self.part.percent


class Result(models.Model):
    """ Результаты машин """
    car = models.OneToOneField('Car', related_name='results', verbose_name='Машина', on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(verbose_name='Итоговая сумма')
    price_car = models.PositiveIntegerField(verbose_name='Себе стоимость')
    benefit = models.PositiveIntegerField(verbose_name='Выгода')

    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Result'

    def __str__(self):
        return self.car.name
