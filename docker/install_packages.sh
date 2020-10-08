#!/bin/sh


if [[ ! -s "/firsttime.lock" ]]; then
    if [[ -s "requirements-firsttime.txt" ]]; then
        pip install -r requirements-firsttime.txt
        date > /firsttime.lock
    fi
fi


if [[ -s "requirements-app.txt" ]]; then
    pip install -r requirements-app.txt
fi
