@echo off
set DJANGO_SETTINGS_MODULE=project.settings
celery -A project beat --loglevel=info