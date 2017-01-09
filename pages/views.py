from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from .models import Faq

class HomeView(TemplateView):
    template_name = "pages/home.html"

class FaqView(View):
    template_name = "dashbord/faq.html"

    def get(self, request):
        faqs = Faq.objects.filter(active=True)
        return render(request, self.template_name,{'faqs':faqs})