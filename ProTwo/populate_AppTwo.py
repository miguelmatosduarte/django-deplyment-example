import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# FAKE POPULATE SCRIPT
import random
from AppTwo.models import User
from faker import Faker

def populate(N=5):

    User.objects.all().delete()

    for entry in range(N):
        fakegen = Faker()
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()
        print(f"First Name: {fake_first_name}; Last Name: {fake_last_name}; Email: {fake_email}")
        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if (__name__ == '__main__'):
    populate(20)
