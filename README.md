# Test Project

## API
- [x] Add order (decorator to check vip and remaining stocks) 
- [x] Delete order (decorator to check remaining stocks)
- [x] Show top 3 popular products
- [x] Save csv file at 00:00
- [x] Use Docker
- [x] Deploy project
- [x] Unit test

## Django Project Structure
```
test
├── csv_dump.py                 # Store csv file
├── data.csv                    # csv file: Number of orders, sales figures, Total sales
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── new_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── decorator.py            # decorator function
│   ├── migrations
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── img
│   │   │   ├── cart.ico
│   │   │   ├── minus.png
│   │   │   └── plus.png
│   │   └── js
│   │       └── top3-button.js  # javascript(ajax) 
│   ├── templates
│   │   └── page.html
│   ├── tests.py                # Unit test
│   ├── urls.py
│   └── views.py    
└── script
    ├── create-app
    ├── insert_data.py
    ├── insert_data_script      # insert stocks into sqlite
    └── start-server            # do migrations, unit test, and run app

```

## Setup
#### 1. Linux Environment
See repository **[Django-docker-test](https://github.com/ArthurWuTW/test-docker)** and follow the instructions to install docker and create docker image.

#### 2. Database
Use Sqlite

#### 3. Configuration
TODO: Secure private data

## Run Server
```sh
# start container
cd <DOCKER_REPO_DIR>/docker
./project-start-container

# enter container
./project-enter-container-shell

# run app
cd <DJANGO_PROJECT_DIR>/script
./start-server
```

## Unit test
#### 1. Click Plus button to add order by VIP customers
```py
driver = webdriver.Firefox(options=options) # Use Selenium.webdriver
...

driver.find_element_by_id('image-btn').click() # Click Plus buttonself.assertEqual(queried_order.product_id, product[0])

# Test assertions
self.assertEqual(queried_order.qty, product[1])
self.assertEqual(queried_order.price, product[2])
self.assertEqual(queried_order.shop_id, product[3])
self.assertEqual(queried_order.customer_id, 'ABC')...

```
#### 2. Click Plus button to order VIP products by non-VIP customer
```py

...
self.assertIn('你不是ｖｉｐ', driver.page_source) # Test assertion

```

#### 3. Click Plus button to order products, but it's understock
```py
# Buy more than stock (stock_pcs+1)
driver.find_element_by_id('product_number').send_keys(str(product[1]+1))

...
self.assertIn('貨源不足', driver.page_source) # Test assertion

```

#### 4. Click minus button to delete the order
```py
# Test assertion
self.assertEqual(len(Order.objects.all()), 0)
self.assertIn('商品到貨', driver.page_source) 

```

