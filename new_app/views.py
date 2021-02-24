from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Product, Order
from functools import wraps

def check_vip_and_stock(function):
    @wraps(function)
    def wrap(self, request, *args, **kwargs):

        print(request.POST)
        # if request.POST.get('isVIP') != None:
        #
        #     return function(request, *args, **kwargs)



        return function(self, request, *args, **kwargs)
    return wrap


class Page(View):
    # @check_vip_and_stock
    def get(self, request):
        render_dict = dict()

        products = Product.objects.all()
        product_array = list()
        for product in products:
            product_array.append([product.product_id, product.stock_pcs, product.price, product.shop_id, str(product.vip).lower()])

        orders = Order.objects.all()
        order_array = list()
        for order in orders:
            order_array.append([order.id, order.product_id, order.qty, order.price, order.shop_id, order.customer_id])


        render_dict['products'] = product_array
        render_dict['orders'] = order_array
        print(order_array)
        render_dict['products'] = product_array
        print(render_dict)
        return render(self.request, 'page.html', render_dict)

    @check_vip_and_stock
    def post(self, request):
        print("========================================")
        print(request.POST.get('product_name'))
        print(request.POST.get('product_number'))
        print(request.POST.get('customer_id'))
        print(request.POST.get('isVIP')) # pass none if unclicked
        print("========================================")
        if request.POST.get('product_name') != None:
            product_name = request.POST.get('product_name')
        order_product = Product.objects.get(product_id=product_name)
        print(order_product)
        order = Order()
        order.product_id = order_product.product_id
        order.qty = request.POST.get('product_number')
        order.price = order_product.price
        order.shop_id = order_product.shop_id
        order.customer_id = request.POST.get('customer_id')
        order.save()
        print("-----------------------------------------")

        print(order.product_id)
        print(order.qty)
        print(order.price)
        print(order.shop_id)
        print(order.id)



        render_dict = dict()
        products = Product.objects.all()
        product_array = list()
        for product in products:
            product_array.append([product.product_id, product.stock_pcs, product.price, product.shop_id, str(product.vip).lower()])

        orders = Order.objects.all()
        order_array = list()
        for order in orders:
            order_array.append([order.id, order.product_id, order.qty, order.price, order.shop_id, order.customer_id])


        render_dict['products'] = product_array
        render_dict['orders'] = order_array
        print(order_array)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(render_dict)
        return render(self.request, 'page.html', render_dict)
