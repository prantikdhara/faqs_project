from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cached_faqs = cache.get(f'faqs_{lang}')
        
        if cached_faqs:
            return Response(cached_faqs)
        
        faqs = FAQ.objects.all()
        data = [faq.get_translation(lang) for faq in faqs]
        cache.set(f'faqs_{lang}', data, timeout=3600)

        return Response(data)