@echo off
cmd /k "cd /d C:\Project\jpdriller-master\jpdriller-master\website & python manage.py runserver"
timeout 2
start http://127.0.0.1:8000/jpdriller/
@echo off
