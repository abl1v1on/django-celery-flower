### Run Redis

~~~linux
sudo docker run --name some-redis -d redis
~~~

### Run Celery

~~~
celery -A DjangoCelery worker -l info
~~~

### Run Flower

~~~
flower -A DjangoCelery --port=5555
~~~

