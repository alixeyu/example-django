#!/bin/sh

gunicorn website.wsgi:app -b 0.0.0.0:8000