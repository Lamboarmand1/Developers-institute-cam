import os
import django
from faker import Faker
from rent.models import Customer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_rental.settings')
django.setup()

#créer un objet de la classe Faker pour utiliser les methodes
f = Faker()

for i in range(101):
    new_customer = Customer(firstname=f.first_name(),
                            lastname=f.last_name(),
                            email=f.email(),
                            phonenumber=f.random_number(),
                            city=f.city(),
                            country=f.country(),
                            address=f.address())
    new_customer.save()
    print(f'created customer {new_customer.firstname}')
    #Customer.objects.create()
print('100 customers created')

