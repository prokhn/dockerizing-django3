FROM python:3.8-slim

#RUN apt-get install libpq-dev python3-dev
RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

ENTRYPOINT python manage.py migrate && \
           python manage.py collectstatic --no-input && \
           python setup.py && \
           /usr/local/bin/gunicorn django_project.wsgi:application -w 2 -b :8000