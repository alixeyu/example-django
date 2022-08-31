#!/bin/sh

gunicorn website.wsgi:application -b 0.0.0.0:8000