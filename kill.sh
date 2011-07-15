#!/bin/bash

if [[ $VIRTUAL_ENV == "" ]]; then
    source env/bin/activate
fi

python kill-database.py
