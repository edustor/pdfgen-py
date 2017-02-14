FROM python:3.6-onbuild
CMD uwsgi --http :9090 --wsgi-file main.py --callable app --master --stats :9191