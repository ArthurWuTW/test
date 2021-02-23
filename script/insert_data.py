print('=============ADD DATA================')

products = [
    [1,	6,	150,	'um',	False],
    [2,	10,	110,	'ms',	False],
    [3,	20,	900,	'ps',	False],
    [4,	2,	1899,	'ps',	True],
    [5,	8,	35,	    'ms',	False],
    [6,	5,	60,	    'um',	False],
    [7,	5,	800,	'ps',	True]
]

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
from new_app.models import Product

for product in products:
    new_data = Product()
    new_data.product_id = product[0]
    new_data.stock_pcs = product[1]
    new_data.price = product[2]
    new_data.shop_id  = product[3]
    new_data.vip  = product[4]

    new_data.save()


print('=====================================')
