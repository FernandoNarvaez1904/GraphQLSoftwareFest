import random
import string
from datetime import timedelta, datetime
from typing import List

from tortoise import fields
from tortoise.models import Model


class Item(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    barcode = fields.CharField(max_length=255)
    cost = fields.FloatField()
    markup = fields.FloatField()
    creationDate = fields.DatetimeField()
    is_active = fields.BooleanField()
    current_stock = fields.FloatField()
    is_service = fields.BooleanField()
    sku = fields.CharField(max_length=255)
    price = fields.FloatField()


async def populate_items(count: int) -> List[Item]:
    result = []
    for _ in range(count):
        item = Item(
            name=''.join(random.choices(string.ascii_letters, k=10)),
            barcode=''.join(random.choices(string.digits, k=10)),
            cost=random.uniform(1.0, 100.0),
            markup=random.uniform(0.1, 0.5),
            creationDate=datetime.now() - timedelta(days=random.randint(1, 365)),
            is_active=random.choice([True, False]),
            current_stock=random.uniform(1.0, 1000.0),
            is_service=random.choice([True, False]),
            sku=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            price=random.uniform(1.0, 1000.0)
        )
        await item.save()
        result.append(item)
    return result
