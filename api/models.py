from pyexpat import model
from xml.etree.ElementInclude import default_loader
from django.db import models
from matplotlib.pyplot import cla
from matplotlib.style import available


class BaseOffer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    base_price = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=True)
    amount_added = models.ManyToManyField('AmountAdded')

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.name + ' ' + str(self.base_price) + self.amount_added.__str__()

    class Meta:
        db_table = 'offer'


class Added(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    amount = models.ManyToManyField(
        'Amount', through='AmountAdded', through_fields=('added', 'amount'))

    def __str__(self) -> str:
        available = 'available ' if self.available else ' '
        return str(self.id) + ' ' + self.name + ' ' + available + self.amount.__str__()

    class Meta:
        db_table = 'added'


class Amount(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    amount_list = models.TextChoices('AmountType', 'Low Medium High')
    amount = models.CharField(max_length=30, choices=amount_list.choices)

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.amount

    class Meta:
        db_table = 'amount'


class AmountAdded(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    added = models.ForeignKey(Added, on_delete=models.CASCADE)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(id) + ' ' + str(self.added) + ' ' + str(self.amount) + str(self.price)

    class Meta:
        db_table = 'ammount_added'
