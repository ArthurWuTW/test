from django.shortcuts import render
from django.views import View

class Page(View):
    def get(self, request):
        return render(self.request, 'template/page.html', contextHandler.getContext())
