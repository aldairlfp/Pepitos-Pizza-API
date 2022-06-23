from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError


def validate_int(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError('{} is not a integer number'.format(value))


class BaseOffer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    offers = models.ManyToManyField(
        'AmountAdded', through='Offer', through_fields=('base_offer', 'amount_added'))
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return 'id_BO: ' + self.id.__str__() + ', name_BO: ' + self.name

    class Meta:
        db_table = 'base_offer'


class Added(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    amount = models.ManyToManyField(
        'Amount', through='AmountAdded', through_fields=('added', 'amount'))
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return 'id_Added: ' + self.id.__str__() + ', name_Added: ' + self.name

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
    available = models.BooleanField(default=True)
    def __str__(self) -> str:
        
        return self.id.__str__() + ' added: ' + self.added.__str__() + ', amount: ' + self.amount.__str__() + ', '

    class Meta:
        db_table = 'amount_added'
        unique_together = ('added', 'amount')


class Offer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    base_offer = models.ForeignKey(BaseOffer, on_delete=models.CASCADE)
    amount_added = models.ForeignKey(AmountAdded, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        available = 'available ' if self.available else ' '
        return str(self.id) + ' ' + self.base_offer.__str__() + ' ' + self.amount_added.__str__() + self.price.__str__() + ' ' + available

    class Meta:
        db_table = 'offer'
        unique_together = ('base_offer', 'amount_added')


class Client(models.Model):
    ci = models.CharField(max_length=11, primary_key=True, validators=[
                          MinLengthValidator(11), MaxLengthValidator(11), validate_int])
    name = models.CharField(max_length=100, validators=[
                            MinLengthValidator(1), MaxLengthValidator(100)])
    address = models.CharField(max_length=100, validators=[
                               MinLengthValidator(1), MaxLengthValidator(100)], null=False)
    orders = models.ManyToManyField(Offer, through='Order', through_fields=('client', 'offer'))

    class Meta:
        db_table = 'client'

        
class OrderList(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100, validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    StateOrder = models.TextChoices('StateOrder', 'Pending Accepted Canceled')
    state_order = models.CharField(max_length=30, choices=StateOrder.choices)
    
    def save(self, *args, **kwargs):
        hash_id = hash(self.id)
        hash_date = hash(self.date)
        hash_address = hash(self.address)
        self.id = hash_id ^ hash_date ^ hash_address
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'order_list'
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    order_list = models.ForeignKey(OrderList, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'order'
        unique_together = ('client', 'offer')

    