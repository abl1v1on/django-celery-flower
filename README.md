### Run Redis

~~~linux
sudo docker run 
~~~

### Run Celery

~~~
celery -A {your_project_name} worker -l info
~~~

### Run Flower

~~~
flower -A {your_project_name} --port=5555
~~~

