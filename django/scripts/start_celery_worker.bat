@echo off
celery -A project worker --loglevel=info --pool=solo -E 