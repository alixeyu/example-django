#!/bin/sh

gunicorn website.wsgi:application