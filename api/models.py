from django.db import models

class BaseOfferORM(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    base_price = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.name + ' ' + str(self.base_price)
    class Meta:
        db_table = 'base_offer'
