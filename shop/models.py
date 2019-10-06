from django.db import models


class User(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    creation_date = models.DateField(auto_now_add=True)

    @property
    def full_name(self):
        return '{} {} {}'.format(self.surname, self.name, self.patronymic)


class ProductCategory(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    production_date = models.DateField()
    color = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()

    @property
    def full_title(self):
        return '{} {} {}'.format(self.manufacturer, self.model, self.color)


class Order(models.Model):
    # STATUS_CHOICES = (('Активный', 'Активный'), ('Отмененённый', 'Отмененённый'))

    email = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    amount = models.PositiveIntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    order_status = models.CharField(max_length=30, default='Активный')

    @property
    def total_cost(self):
        return self.amount * self.product.cost
