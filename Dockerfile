FROM python:2.7-slim

RUN apt update && apt install -y \
    gcc \
    python-dev \
    build-essential \
    libpq-dev \
    libevent-dev \
    unoconv

RUN pip install Cython

COPY deps.pip .
RUN python -m pip install -r deps.pip

WORKDIR /app
COPY . /app

EXPOSE 8000

# RUN ./load_initial_data.sh
CMD python manage.py syncdb && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
