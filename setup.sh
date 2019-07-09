#!/bin/bash
#python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
bower install
python manage.py migrate
python manage.py add_data
python manage.py runserver 0.0.0.0:8888