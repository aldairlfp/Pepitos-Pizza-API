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
    amount_added = models.ManyToManyField(
        'AmountAdded', through='Offer', through_fields=('base_offer', 'amount_added'))

    def __str__(self) -> str:
        return 'id_BO: ' + self.id.__str__() + ', name_BO: ' + self.name + ', price_BO: ' + self.base_price.__str__()

    class Meta:
        db_table = 'base_offer'


class Added(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    amount = models.ManyToManyField(
        'Amount', through='AmountAdded', through_fields=('added', 'amount'))

    def __str__(self) -> str:
        available = 'available ' if self.available else ' '
        return 'id_Added: ' + self.id.__str__() + ', name_Added: ' + self.name + ', ' + available

    class Meta:
        db_table = 'added'


class Amount(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    amount_list = models.TextChoices('AmountType', 'Low Medium High')
    amount = models.CharField(max_length=30, choices=amount_list.choices)

    def __str__(self) -> str:
        return 'id_Amount: ' + self.id.__str__() + ', amount: ' + self.amount

    class Meta:
        db_table = 'amount'


class AmountAdded(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    added = models.ForeignKey(Added, on_delete=models.CASCADE)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.id.__str__() + ' added: ' + self.added.__str__() + ', amount: ' + self.amount.__str__() + ', price: '+self.price.__str__()

    class Meta:
        db_table = 'ammount_added'


class Offer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    base_offer = models.ForeignKey(BaseOffer, on_delete=models.CASCADE)
    amount_added = models.ForeignKey(AmountAdded, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.base_offer.__str__() + ' ' + self.amount_added.__str__()

    class Meta:
        db_table = 'offer'
