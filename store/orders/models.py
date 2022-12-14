from django.db import models

from products.models import Basket
from users.models import User


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен')
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total_sum = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Order #{self.id} for {self.first_name} {self.last_name}'

    def order_paid(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.basket_history =\
            {
                'purchased': [basket.json_basket() for basket in baskets],
                'total_sum': float(baskets.total_sum()),

            }
        self.status = self.PAID
        baskets.delete()
        self.save()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
