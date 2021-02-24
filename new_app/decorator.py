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
                request.POST.update({'status': ''})
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
