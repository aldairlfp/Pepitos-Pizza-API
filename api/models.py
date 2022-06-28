import ctypes

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError


def validate_int(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError('{} is not a integer number'.format(value))


class BaseOffer(models.Model):
    name = models.CharField(max_length=100)
    avaidable = models.BooleanField(default=True)
    addeds = models.ManyToManyField('Added')
    price = models.PositiveSmallIntegerField()
    
    def avaidable_addeds(self):
        return self.addeds.filter(avaidable=True)

    def __str__(self) -> str:
        return 'id_BO: {}, name_BO: {}, addeds: {}'.format(self.id.__str__(), self.name, self.addeds.filter(avaidable=True))

    class Meta:
        db_table = 'base_offer'


class Added(models.Model):
    name = models.CharField(max_length=100)
    avaidable = models.BooleanField(default=True)
    price = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return 'id_Added: ' + self.id.__str__() + ', name_Added: ' + self.name

    class Meta:
        db_table = 'added'

class RequestedOffer(models.Model):
    base_offer = models.ForeignKey(BaseOffer, on_delete=models.CASCADE)
    addeds = models.ManyToManyField(Added)

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.base_offer.__str__() + ' ' + self.addeds.__str__() + ' '

    class Meta:
        db_table = 'requested_offer'


class Client(models.Model):
    ci = models.CharField(max_length=11, primary_key=True, validators=[
                          MinLengthValidator(11), MaxLengthValidator(11), validate_int])
    name = models.CharField(max_length=100, validators=[
                            MinLengthValidator(1), MaxLengthValidator(100)])
    address = models.CharField(max_length=100, validators=[
                               MinLengthValidator(1), MaxLengthValidator(100)], null=False)

    class Meta:
        db_table = 'client'


class OrderList(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    StateOrder = models.TextChoices('StateOrder', 'Pending Accepted Canceled')
    state_order = models.CharField(max_length=30, choices=StateOrder.choices, default=StateOrder.Pending)

    def save(self, *args, **kwargs):
        hash_id = hash(self.id)
        hash_date = hash(self.date)
        hash_client = hash(self.client.ci)
        id_c = ctypes.c_ulong(hash_id).value
        date_c = ctypes.c_ulong(hash_date).value
        client_c = ctypes.c_ulong(hash_client).value
        id = hex(id_c ^ date_c ^ client_c)
        self.id = id
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'order_list'


class Order(models.Model):
    requested_offer = models.ForeignKey(RequestedOffer, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    order_list = models.ForeignKey(OrderList, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'