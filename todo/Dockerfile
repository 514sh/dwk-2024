FROM python:3.12-alpine

WORKDIR /usr/src/app

COPY app.py requirements.txt /usr/src/app/
COPY templates /usr/src/app/templates

RUN pip install -r requirements.txt && mkdir static

CMD ["python3", "app.py"]