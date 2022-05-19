from django.db import models

class BaseOfferORM(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    base_price = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'base_offer'
