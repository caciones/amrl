# AMRL

## Setup

1. Create a Python virtual environment by running
    `python -m venv venv`
2. Activate Python environment
    `source venv/bin/activate`
3. Install the Python packages
    `pip install -r requirements.txt`
4. Create `.env` from `env.sample`
    - to connect to an external database, configure the matching variables in env
5. Check `Makefile` for the available commands

## GDAL requirements in Ubuntu

Make sure the following are installed

```bash
apt-get install -y binutils libproj-dev gdal-bin
```

## Docker
### Docker Compose

> Do not forget to check Makefile

Start services in docker compose

```bash
docker compose up -d
```

Stop all the services in docker compose

```bash
docker compose down
```

### Docker run

```bash
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
```
## Django
### Generate migrations (database tables)

```bash
python manage.py makemigrations
```

### Run migrations (create tables in the database)

```bash
python manage.py migrate
```

## Python packages
### Install requirements.txt

```bash
pip install -r requirements.txt 
```

### Update requirements.txt


```bash
pip freeze > requirements.txt 
```
