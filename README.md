# Plant Monitor

## API
- [x] Add order (decorator to check vip and remaining stocks) 
- [x] Delete order (decorator to check remaining stocks)
- [x] Show top 3 popular products
- [x] Save csv file at 00:00
- [x] Use Docker
- [x] Deploy project
- [ ] Unit test


## Django Project Structure
```
test
├── csv_dump.py                 # Store csv
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
│   ├── tests.py                # TODO - unit test
│   ├── urls.py
│   └── views.py    
└── script
    ├── create-app
    ├── insert_data.py
    ├── insert_data_script      # insert stocks into sqlite
    └── start-server            # run script

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
