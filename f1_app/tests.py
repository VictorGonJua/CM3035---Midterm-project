from datetime import date
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from rest_framework import status
from .models import *
from .factories import *
from .serializers import *
from .views import *

# Create your tests here.

class CircuitModelTest(TestCase):
    def setUp(self):
        self.circuit = CircuitFactory.create()
    def tearDown(self):
        Circuit.objects.all().delete()
    def test_circuit_creation(self):
        self.assertIsNotNone(self.circuit.circuitId) 
        self.assertTrue(isinstance(self.circuit.name, str) and self.circuit.name.startswith("Circuit"))
        self.assertTrue(isinstance(self.circuit.location, str))
        self.assertTrue(isinstance(self.circuit.country, str))
        self.assertTrue(isinstance(self.circuit.circuitRef, str))
        self.assertTrue(isinstance(self.circuit.lat, float))
        self.assertTrue(isinstance(self.circuit.lng, float))
        self.assertTrue(isinstance(self.circuit.url, str) and self.circuit.url.startswith("http://"))

class DriverModelTest(TestCase):
    def setUp(self):
        self.driver = DriverFactory.create()
    def tearDown(self):
        Driver.objects.all().delete()
    def test_driver_creation(self):
        self.assertIsNotNone(self.driver.driverId) 
        self.assertTrue(isinstance(self.driver.forename, str))
        self.assertTrue(isinstance(self.driver.surname, str))
        self.assertTrue(isinstance(self.driver.dob, date))
        self.assertTrue(isinstance(self.driver.driverRef, str))
        self.assertTrue(isinstance(self.driver.number, str))
        self.assertTrue(isinstance(self.driver.code, str))
        self.assertTrue(isinstance(self.driver.nationality, str))

class CircuitListViewTest(APITestCase):
    def setUp(self):
        CircuitFactory.create_batch(5)
    def test_list_circuits(self):
        url = reverse('circuit-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(len(response.data), 5)

class DriverSerializerTest(TestCase):
    def setUp(self):
        self.driver_attributes = {
            'forename': 'Lewis',
            'surname': 'Hamilton',
            'driverId': 44,
            'code': 'HAM',
            'nationality': 'British',
            'dob': '1985-01-07'
        }
        self.driver = DriverFactory(**self.driver_attributes)
        self.serializer = DriverSerializer(instance=self.driver)
    def test_contains_expected_fields(self):
        data = self.serializer.data
        expected_fields = {'forename', 'surname', 'code', 'nationality', 'dob', 'url', 'number', 'driverRef'}
        self.assertEqual(set(data.keys()), expected_fields)
    def test_field_content(self):
        data = self.serializer.data
        for field_name in ['forename', 'surname', 'code', 'nationality', 'dob']:
            if field_name in data:
                self.assertEqual(data[field_name], self.driver_attributes[field_name])


class URLTests(SimpleTestCase):
    def test_circuit_list_url_resolves(self):
        url = reverse('circuit-list')
        self.assertEqual(resolve(url).func.view_class, CircuitListView)
