# Запуск
- в консоли перейти в директорию с проектом
- python3 -m venv env
- source env/bin/activate
- pip3 install -r requirements.txt
- python3 manage.py makemigrations shop
- python3 manage.py migrate
- python3 manage.py runserver

# Описание API

- получение, создание, редактирование и удаление пользователей

`GET api/v1/users/`

`POST api/v1/users/create/`

`GET api/v1/users/<user_id>/`

`PUT/PATCH api/v1/users/<user_id>/edit/`

`DELETE api/v1/users/<user_id>/delete/`
- получение, создание, редактирование и удаление пользователей

`GET api/v1/tasks/`

`POST api/v1/tasks/create/`

`GET api/v1/tasks/<task_id>/`

`PUT/PATCH api/v1/tasks/<task_id>/edit/`

`DELETE api/v1/tasks/<task_id>/delete/`
- поиск и фильтрация пользователей по должности

`GET api/v1/users/?search=<role>`

- поиск и фильтрация задач по названию

`GET api/v1/tasks/?search=<name>`

- назначение/снятие назначения задачи на пользователя

`PATCH api/v1/tasks/<task_id>/edit/`: "{'assigned': <user_id>}"

`PATCH api/v1/tasks/<task_id>/edit/`: "{'assigned': null}"

- назначение пользователя, который сможет проверить выполнение конкретной задачи конкретным пользователем (саму проверку и статусы выполнения задачи реализовывать не нужно)

`PATCH api/v1/tasks/<task_id>/edit/`: "{'reviewer': <user_id>}"

`PATCH api/v1/tasks/<task_id>/edit/`: "{'reviewer': null}"

- получение всех задач, назначенных пользователю — с проверяющими, когда они есть

`GET api/v1/tasks/assigned-to/<user_id>/`

- получение всех пользователей, кому назначена задача

`GET api/v1/tasks/?with_task=true`
