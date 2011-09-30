#!/bin/bash

# creates a virtual python environment and installs all
# dependencies
# DOES NOT setup the database

virtualenv -p python2 env
. env/bin/activate
pip install --upgrade flask
pip install --upgrade flask-sqlalchemy
pip install --upgrade flask-wtf
#pip install --upgrade flask-login
pip install --upgrade flask-markdown
#pip install --upgrade python-dateutil
