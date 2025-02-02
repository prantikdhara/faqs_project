from django.test import TestCase

# Create your tests here.
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation_method(self):
        faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
        self.assertEqual(faq.get_translation('en')['question'], "What is Django?")