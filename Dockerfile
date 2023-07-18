FROM python:3.11.1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/code/
# Create a working directory for the django project
WORKDIR /code
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin --no-install-recommends

# Copy requirements to the container
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the project files into the working directory
COPY . /code/

RUN mkdir static

RUN python manage.py collectstatic --noinput

RUN adduser appuser
USER appuser
CMD python manage.py runserver 0.0.0.0:8000

# gunicorn core.wsgi:application