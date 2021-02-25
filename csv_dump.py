import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import sqlite3
import pandas
import numpy as np
import pandas as pd
import os
import schedule
import time




def job():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    conn = sqlite3.connect(dir_path+'/db.sqlite3')

    data = list()
    data.append(['館別', '總銷售金額', '總銷售數量', '總訂單數量'])
    for order in conn.execute('SELECT shop_id, SUM(qty*price) AS sum_price, SUM(qty) AS sum_qty, COUNT(id) as order_number FROM new_app_order GROUP BY shop_id ORDER BY shop_id;'):
        data.append(np.array(order))

    pd.DataFrame(data).to_csv(dir_path+"/data.csv")

schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
