#!/bin/sh

gunicorn website.wsgi:application --daemon