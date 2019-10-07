# Запуск сервера
- в консоли перейти в директорию с проектом
- pip install -r requirements.txt
- python manage.py makemigrations shop
- python manage.py migrate
- python manage.py runserver

# Описание API

- получение, создание, редактирование и удаление пользователей

`POST /users/create/`

{
  "surname": "Alexeev",
	"name": "Anton",
	"patronymic": "Ivanovich",
  "email": "6aka@mail.ru"
}

`GET /users/`

`GET /users/<user_id>/`

`PUT /users/<user_id>/edit/`

{
  "surname": "Sidorov",
	"name": "Anton",
	"patronymic": "Ivanovich",
  "email": "6aka@mail.ru"
}

`PATCH /users/<user_id>/edit/`

{
  "name": "Semen"
}

`DELETE /users/<user_id>/delete/`

- получение, создание, редактирование и удаление категорий товаров

`POST /category/create/`

{
  "title": "Телевизоры",
	"url": "TVs"
}

`GET /category/`

`GET /category/<category_id>/`

`PUT /category/<category_id>/edit/`

{
  "title": "Телевизоры",
	"url": "TV"
}

`PATCH /category/<category_id>/edit/`

{
	"url": "TVs"
}

`DELETE /category/<category_id>/delete/`

- получение, создание, редактирование и удаление товаров

`POST /product/create/`

{
  "category": 1,
	"manufacturer": "Samsung",
	"model": "25001T",
	"production_date": "2016-10-03",
	"color": "Чёрный",
	"cost": "18000"
}

`GET /product/`

`GET /product/<category_id>/`

`PUT /product/<product_id>/edit/`

{
  "category": 1,
	"manufacturer": "Samsung",
	"model": "25001T",
	"production_date": "2016-10-03",
	"color": "Чёрный",
	"cost": "20000"
}

`PATCH /product/<product_id>/edit/`

{
  "color": "Белый"
}

`DELETE /product/<product_id>/delete/`

- получение, создание, отмена заказов

`POST /order/create/`

{
  "email": "6aka@mail.ru",
	"product": 1,
	"amount": 2,
  "comment": ""
}

`GET /order/`

`PATCH /order/<order_id>/cancel/`

- фильтрация заказов по статусу

`GET /order/?search=<status>`

- поиск заказов по email

`GET /order/?search=<email>`

