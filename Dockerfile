FROM python:3.6
RUN apt update && apt install -y libqrencode-dev
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD uwsgi --http :9090 --wsgi-file main.py --callable app --master --stats :9191