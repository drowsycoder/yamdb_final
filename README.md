# YaMDb

Учебный проект YaMDb представляет собой базу данных произведений, разделенных на категории и жанры.
Пользователи могут оставлять к произведениям отзывы, а к отзывам - комментарии.

API проекта основан на Django REST Framework.
Административная панель: http://localhost/admin/


### Предварительные требования

Необходимо установить Docker с официального [сайта](https://www.docker.com/products/docker-desktop).


### Информация по работе с проектом

0. Клонирование проекта:
```
git clone https://github.com/drowsycoder/infra_sp2.git
```   
1. Загрузка контейнеров с [DockerHub](https://hub.docker.com/repository/docker/drowzycoder/infra_sp2) и запуск (из корневой директории проекта при активном Docker):

Создайте файл .env с переменными окружения. Например, так:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Запустите контейнеры:
```
docker pull drowzycoder/infra_sp2
docker-compose up
```
2. Вход в командную оболочку внутри контейнера:
```
docker exec -it <container_id> bash
```
3. Тестирование в командной оболочке контейнера:
```
pytest
```
4. Миграции в командной оболочке контейнера:
```
python manage.py migrate
```
5. Создание суперпользователя в командной оболочке контейнера:
```
python manage.py createsuperuser
```
6. Заполнение БД фикстурами:
```
docker-compose exec web python manage.py loaddata fixtures.json
```
