import factory
from .models import *

class CircuitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Circuit
    name = factory.Sequence(lambda n: f"Circuit {n}")
    location = factory.Faker('city')
    country = factory.Faker('country')
    circuitRef = factory.Sequence(lambda n: f"ref_{n}")
    lat = 25.000000
    lng = 50.000000
    url = factory.Sequence(lambda n: f"http://www.test.com/circuit{n}")


class DriverFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Driver
    forename = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    dob = factory.Faker('date_of_birth', minimum_age=18, maximum_age=40)
    driverRef = factory.Sequence(lambda n: f"driver_{n}")
    number = factory.Sequence(lambda n: f"{n:02d}")  
    code = factory.Sequence(lambda n: f"CD{n:02d}")
    nationality = factory.Faker('country_code')

