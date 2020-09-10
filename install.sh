#!/usr/bin/env bash

# Make Sure you have set up a virtual environment before running this script.

# Set the ENV variable to LOCAL
export ENV=LOCAL

# Install dependencies
pip install -r requirements.txt

# Migrate the database
python manage.py migrate

# Create the Default Roles: Trader, Approver, Admin
python manage.py create_roles
# Create test Orders
python manage.py create_orders

# Run the local webserver
./manage.py runserver 8000
