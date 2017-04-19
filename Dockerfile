FROM python:3.6
RUN apt update && apt install -y libqrencode-dev
WORKDIR /code

ADD requirements.txt /code
RUN pip3 install -r requirements.txt

ADD . /code
ARG test=false
RUN if $test; then\
    pip3 install -r test-requirements.txt; \
    pytest; \
    fi

CMD uwsgi --http :9090 --wsgi-file main.py --callable app --master --stats :9191