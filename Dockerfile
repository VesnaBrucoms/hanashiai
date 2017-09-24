from python:3.6

COPY ./requirements/ /tmp/hanashiai/
RUN pip install -r /tmp/hanashiai/base.txt

COPY ./django/ /opt/hanashiai/
WORKDIR /opt/hanashiai/

EXPOSE 4431

CMD ./gunicorn_start.sh