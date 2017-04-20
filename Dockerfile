FROM python:3.6
RUN apt update && apt install -y libqrencode-dev
WORKDIR /code

ADD requirements.txt /code
RUN pip3 install -r requirements.txt

ADD . /code

CMD uwsgi --http :8080 --wsgi-file main.py --callable app --master --stats :8081