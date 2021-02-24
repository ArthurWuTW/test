from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Product, Order


class Page(View):
    def get(self, request):
        render_dict = dict()

        products = Product.objects.all()
        product_array = list()
        for product in products:
            product_array.append([product.product_id, product.stock_pcs, product.price, product.shop_id, str(product.vip).lower()])

        render_dict['products'] = product_array
        print(render_dict)
        return render(self.request, 'page.html', render_dict)

    def post(self, request):
        print("213")
        print(request.POST.get('product_name'))
        print(request.POST.get('product_number'))
        print(request.POST.get('customer_id'))

        render_dict = dict()

        products = Product.objects.all()
        product_array = list()
        for product in products:
            product_array.append([product.product_id, product.stock_pcs, product.price, product.shop_id, str(product.vip).lower()])

        render_dict['products'] = product_array
        print(render_dict)
        return render(self.request, 'page.html', render_dict)
