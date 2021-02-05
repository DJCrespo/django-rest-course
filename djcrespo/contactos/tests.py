from django.test import TestCase
from .models import Contact

# Create your tests here.
class PostTest(TestCase):

    def setUp(self):    #10 examples of ORM Create
        #1
        instance = Contact.objects.create(name='Didier', phone='9992350960', email='dj.crespo.castilla@gmail.com')
        instance.save()
        #2
        instance = Contact.objects.create(name='Jesus', phone='', email='')
        instance.save()
        #3
        name = 'Gabriela'
        phone = '9991275756'
        email = ''
        instance = Contact.objects.create(name=name, phone=phone, email=email)
        instance.save()
        #4
        name2 = input('name: ')
        phone2 = input('phone: ')
        instance = Contact.objects.create(name=name2, phone=phone2)
        #5
        instance = Contact.objects.create(name='Max', phone='9992009901', email='dj.crespo.castilla@hotmail.com')
        instance.save()
        #6
        name3 = input("nombre: ")
        phone3 = input("telefono: ")
        email3 = input("email: ")
        instance = Contact.objects.create(name=name3, phone=phone3, email=email3)
        #7
        instance.name = 'Didier Crespo'
        instance.phone = '9992350960'
        instance.email = ''
        instance.save()
        #8


    def test_for_contact(self): 
        #10 examples of ORM List/Filter/Order
        #1
        print(Contact.objects.all())
        #2
        print(Contact.objects.filter(phone = ''))
        #3
        print(Contact.objects.filter(phone='9992195158'))
        #4
        print(Contact.objects.get(pk=2))
        #5
        query = Contact.objects.all()
        print(query.order_by('name'))
        #6
        query = Contact.objects.all()
        print(query.order_by('-name'))
        #7
        print(Contact.objects.filter(phone='9992350960').order_by('-name'))
        #8
        print(Contact.objects.get(pk=3))

        #10 examples of ORM Get