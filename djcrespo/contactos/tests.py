from django.test import TestCase
from .models import Contact

# Create your tests here.
class TestCase(TestCase):

    def setup(self):
        instance = Contact.objects.create(name='Didier', phone='9992350960', email='dj.crespo.castilla@gmail.com')
        instance.save()