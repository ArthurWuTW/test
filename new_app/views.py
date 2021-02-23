from django.shortcuts import render

# Create your views here.
from django.views import View

class Page(View):
    def get(self, request):
        return render(self.request, 'page.html', {})
