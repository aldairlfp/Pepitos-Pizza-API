from pickle import TRUE
from selectors import BaseSelector
from django.test import TestCase
from matplotlib.style import available

from ..models import Added, BaseOffer, RequestedOffer, Client


class BaseOfferTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ad1 = Added.objects.create(id = 1, name = "queso", price = 10)
        ad2 = Added.objects.create(id = 2, available = False, name = "jamon", price = 15)
        ad3 = Added.objects.create(id = 3, name = "cebolla", price = 7)

        b1 = BaseOffer.objects.create(
            id=1, name="pizza", price=10)
        b1.addeds.set([ad1, ad2, ad3])
        
    def test_id_label(self):
        base_offer = BaseOffer.objects.get(id=1)
        field_label = base_offer._meta.get_field('id').verbose_name
        self.assertEqual(field_label, 'id')

    def test_name_label(self):
        base_offer = BaseOffer.objects.get(id=1)
        field_label = base_offer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_available_label(self):
        base_offer = BaseOffer.objects.get(id=1)
        field_label = base_offer._meta.get_field('available').verbose_name
        self.assertEqual(field_label, 'available')

    def test_addeds_label(self):
        base_offer = BaseOffer.objects.get(id=1)
        field_label = base_offer._meta.get_field('addeds').verbose_name
        self.assertEqual(field_label, 'addeds')

    def test_price_label(self):
        base_offer = BaseOffer.objects.get(id=1)
        field_label = base_offer._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_name_max_length(self):
        base_offer = BaseOffer.objects.get(id=1)
        max_length = base_offer._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_object_stringify_is_correctly_formated(self):
        base_offer = BaseOffer.objects.get(id = 1)
        expected_object_name = f'id_BO: {base_offer.id}, name_BO: {base_offer.name}, addeds: {base_offer.addeds.filter(available=True)}'
        self.assertEqual(str(base_offer), expected_object_name)

    #TODO: Ver como se hace bien el request de los addeds
    # def test_objects_available_addeds_are_available(self):
    #     base_offer = BaseOffer.objects.get(id = 1)
    #     print(base_offer._meta.get_field('addeds'))
    #     expected_addeds = [base_offer._meta.get_field('addeds')]
    #     self.assertEqual(base_offer.available_addeds, expected_addeds)

class AddedTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Added.objects.create(id = 1, name = "queso", price = 10)
        
    def test_id_label(self):
        added_offer = Added.objects.get(id=1)
        field_label = added_offer._meta.get_field('id').verbose_name
        self.assertEqual(field_label, 'id')

    def test_name_label(self):
        added_offer = Added.objects.get(id=1)
        field_label = added_offer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_available_label(self):
        added_offer = Added.objects.get(id=1)
        field_label = added_offer._meta.get_field('available').verbose_name
        self.assertEqual(field_label, 'available')

    def test_price_label(self):
        added_offer = Added.objects.get(id=1)
        field_label = added_offer._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_name_max_length(self):
        added_offer = Added.objects.get(id=1)
        max_length = added_offer._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_object_stringify_is_correctly_formated(self):
        added_offer = Added.objects.get(id = 1)
        expected_object_name = f'id_Added: {added_offer.id}, name_Added: {added_offer.name}'
        self.assertEqual(str(added_offer), expected_object_name)

class RequestedOfferTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        # Set up non-modified objects used by all test methods
        ad1 = Added.objects.create(id = 1, name = "queso", price = 10)
        ad2 = Added.objects.create(id = 2, available = False, name = "jamon", price = 15)
        ad3 = Added.objects.create(id = 3, name = "cebolla", price = 7)

        bo = BaseOffer.objects.create(id=1, name="espaguetti", price=10)
        bo.addeds.set([ad1, ad2, ad3])
       
        ro = RequestedOffer.objects.create(id = 1, base_offer = bo)
        ro.addeds.set([ad1, ad3])
        
    def test_id_label(self):
        requested_offer = RequestedOffer.objects.get(id=1)
        field_label = requested_offer._meta.get_field('id').verbose_name
        self.assertEqual(field_label, 'id')

    def test_addeds_label(self):
        requested_offer = RequestedOffer.objects.get(id=1)
        field_label = requested_offer._meta.get_field('addeds').verbose_name
        self.assertEqual(field_label, 'addeds')

    def test_base_offer_label(self):
        requested_offer = RequestedOffer.objects.get(id=1)
        field_label = requested_offer._meta.get_field('base_offer').verbose_name
        self.assertEqual(field_label, 'base offer')

    def test_object_stringify_is_correctly_formated(self):
        requested_offer = RequestedOffer.objects.get(id = 1)
        expected_object_name = f'{requested_offer.id} {requested_offer.base_offer} {requested_offer.addeds} '
        self.assertEqual(str(requested_offer), expected_object_name)

class ClientTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(ci = 1, name = "Ramon", address = "Ninguna parte")
        
    def test_ci_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('ci').verbose_name
        self.assertEqual(field_label, 'ci')

    def test_name_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_address_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_name_max_length(self):
        base_offer = BaseOffer.objects.get(id=1)
        max_length = base_offer._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_address_max_length(self):
        base_offer = BaseOffer.objects.get(id=1)
        max_length = base_offer._meta.get_field('address').max_length
        self.assertEqual(max_length, 100)

