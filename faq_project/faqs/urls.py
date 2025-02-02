from django.urls import path
from .views import FAQView

urlpatterns = [
    path('faqs/', FAQView.as_view(), name='faq-list'),
]