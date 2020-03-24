## Django 3.0 + PostgreSQL + Nginx development in Docker

With using Celery and Redis
  
* * *
Featuring:
- Docker v19.03.8
- Docker Compose v1.25.4
- Python 3.8.2

* * *
### Deployment Instructions
Rename `.env-sample` to `.env` and set required properties.  
Then run
```
docker-compose build
docker-compose up -d
```
To restart Docker after applying some changes, use
```
docker-compose up --build --force-recreate
```