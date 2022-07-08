from django.db.models.signals import post_save
from django.dispatch import receiver
from car.models import CarPart, Result


@receiver(post_save, sender=CarPart, dispatch_uid="update_stock_count")
def create_result(sender, instance, **kwargs):
    try:
        Result.objects.create(
            car=instance.car,
            total_price=instance.car.total_price,
            price_car=instance.car.price_car,
            benefit=instance.car.benefit,
        )
    except Exception as e:
        raise ValueError(str(e))
