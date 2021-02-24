from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View
from .models import Product, Order
from functools import wraps

def check_vip_and_stock(function):
    @wraps(function)
    def wrap(self, request, *args, **kwargs):
        request.POST._mutable = True
        if request.POST.get('product_name') != None:
            product_name = request.POST.get('product_name')
        ordered_product = Product.objects.get(product_id=product_name)
        if ordered_product.vip == True and request.POST.get('isVIP') == None:
            request.POST.update({'status': 'you are not vip', 'do_order':False})
        elif ordered_product.stock_pcs < int(request.POST.get('product_number')):
            request.POST.update({'status': 'Understock', 'do_order':False})
        else:
            request.POST.update({'status': 'Succeed', 'do_order':True})
        request.POST._mutable = False
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
        if request.POST.get('do_order'):
            print(request.POST.get('status'))
            # print("========================================")
            # print(request.POST.get('product_name'))
            # print(request.POST.get('product_number'))
            # print(request.POST.get('customer_id'))
            # print(request.POST.get('isVIP')) # pass none if unclicked
            # print("========================================")
            if request.POST.get('product_name') != None:
                product_name = request.POST.get('product_name')
            ordered_product = Product.objects.get(product_id=product_name)
            ordered_product.stock_pcs -= int(request.POST.get('product_number'))
            ordered_product.save()

            print(ordered_product)
            order = Order()
            order.product_id = ordered_product.product_id
            order.qty = request.POST.get('product_number')
            order.price = ordered_product.price
            order.shop_id = ordered_product.shop_id
            order.customer_id = request.POST.get('customer_id')
            order.save()
            # print("-----------------------------------------")

            # print(order.product_id)
            # print(order.qty)
            # print(order.price)
            # print(order.shop_id)
            # print(order.id)



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
        # print(order_array)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(render_dict)
        return render(self.request, 'page.html', render_dict)
