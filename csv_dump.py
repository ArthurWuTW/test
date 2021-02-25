import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import sqlite3
import pandas
import numpy as np
import pandas as pd

conn = sqlite3.connect('db.sqlite3')

data = list()
data.append(['館別', '總銷售金額', '總銷售數量', '總訂單數量'])
for order in conn.execute('SELECT shop_id, SUM(qty*price) AS sum_price, SUM(qty) AS sum_qty, COUNT(id) as order_number FROM new_app_order GROUP BY shop_id ORDER BY shop_id;'):
    data.append(np.array(order))

pd.DataFrame(data).to_csv("data.csv")
