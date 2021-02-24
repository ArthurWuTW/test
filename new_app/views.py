from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.views import View
from .models import Product, Order
from functools import wraps

def check_vip_and_stock(function):
    @wraps(function)
    def wrap(self, request, *args, **kwargs):
        request.POST._mutable = True
        if request.POST.get('delete_order_name'):
            # do somethon
            order = Order.objects.get(id=request.POST.get('delete_order_name'))
            ordered_product = Product.objects.get(product_id=order.product_id)
            if ordered_product.stock_pcs==0:
                request.POST.update({'status': '商品到貨'})
        else:
            if request.POST.get('product_name') != None:
                product_name = request.POST.get('product_name')
            ordered_product = Product.objects.get(product_id=product_name)

            if ordered_product.vip == True and request.POST.get('isVIP') == None:
                request.POST.update({'status': '你不是ｖｉｐ！', 'do_order':False})
            elif ordered_product.stock_pcs < int(request.POST.get('product_number')):
                request.POST.update({'status': '貨源不足', 'do_order':False})
            else:
                request.POST.update({'status': '', 'do_order':True})
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
        render_dict['products'] = product_array
        return render(self.request, 'page.html', render_dict)

    @check_vip_and_stock
    def post(self, request):
        render_dict = dict()
        if request.POST.get('do_order'):
            if request.POST.get('product_name') != None:
                product_name = request.POST.get('product_name')
            ordered_product = Product.objects.get(product_id=product_name)
            ordered_product.stock_pcs -= int(request.POST.get('product_number'))
            ordered_product.save()

            order = Order()
            order.product_id = ordered_product.product_id
            order.qty = request.POST.get('product_number')
            order.price = ordered_product.price
            order.shop_id = ordered_product.shop_id
            order.customer_id = request.POST.get('customer_id')
            order.save()
        elif request.POST.get('delete_order_name'):
            order = Order.objects.get(id=request.POST.get('delete_order_name'))
            ordered_product = Product.objects.get(product_id=order.product_id)

            ordered_product.stock_pcs += order.qty
            ordered_product.save()
            order.delete()

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
        render_dict['status'] = request.POST.get('status')
        return render(self.request, 'page.html', render_dict)
