![](https://img.shields.io/badge/Python-3.7.5-blue) 
![](https://img.shields.io/badge/Django-2.2.16-green)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.4-red)
![](https://img.shields.io/badge/Docker-3.8-yellow)
<br>
![example workflow](https://github.com/salexsays/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
<br><br>
## Название проекта
**«YaMDb API»** - проект позволяет оставлять отзывы на произведения различных жанров(музыка. фильмы итд).

**Возможности:**<br>
:black_small_square: Регистрация и авторизация, получение токена, изменение данных своей учетной записи<br>
:black_small_square: Разделение прав пользователей согласно, назначенной ему роли<br>
:black_small_square: Получение, добавление и удаление - категорий, жанров, произведений, отзывов, комментариев и рейтингов<br>
:black_small_square: Администрирование пользователей<br><br>

## :computer: Технологии
:small_blue_diamond: Python <br>
:small_blue_diamond: Django <br>
:small_blue_diamond: Django REST Framework <br>
:small_blue_diamond: DRF Simple JWT <br>
:small_blue_diamond: Docker <br>
:small_blue_diamond: PostgreSQL <br>
:small_blue_diamond: Gunicorn <br>
:small_blue_diamond: Nginx <br>

## :rocket: Запуск проекта
- Склонируйте репозиторий:
```sh
git clone https://github.com/salexsays/yamdb_final.git
```
- Создайте .env файл внутри директории infra:<br>
Пример .env файла:
```sh
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123
DB_HOST=db
DB_PORT=5432
```
-  Запустите docker-compose:
```sh
docker-compose up -d
```
- Выполните миграции, создайте суперпользователя и перенесите статику:
```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
- Наполните базу данных тестовыми данными:
```sh
docker-compose exec -ti web python manage.py loaddata fixtures.json
или
docker-compose exec web python manage.py from_csv
```
- Проверьте доступность сервиса:
```sh
http://localhost/admin
```
### :closed_book: Документация доступна по ссылке:
```sh
http://localhost/redoc/
```

## :bust_in_silhouette: Автор проекта 

### :small_orange_diamond: Алексей Селезнёв
```html
e-mail: salex_n@inbox.ru
```
```html
https://github.com/salexsays
```
## :scroll: Лицензия
```sh
MIT License
```

### :wrench: Проект доступен по ссылке:
```sh
http://salexsays.ddns.net/api/v1/
<br>
<br>
84.252.139.188
```
