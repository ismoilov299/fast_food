from django.db import models

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    lang_id = models.IntegerField(null=True, blank=True)
    chat_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.chat_id)

    class Meta:
        # db_table = 'user'
        # managed = False
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'


class Category(models.Model):
    name_uz = models.CharField(max_length=150)
    name_ru = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150, null=True, blank=True)
    parent = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name_uz}'

    class Meta:
        # db_table = 'category'
        # managed = False
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name_uz = models.CharField(max_length=150)
    name_ru = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    description_uz = models.TextField(null=False, blank=False)
    description_ru = models.TextField(null=False, blank=False)
    description_en = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.name_uz}'

    class Meta:
        # db_table = 'product'
        # managed = False
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField()
    payment_type = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

class About(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.text_uz}'

    class Meta:
        # db_table = 'about_us'
        # managed = False
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Comment(models.Model):
    user_id = models.IntegerField()
    comment_text = models.TextField()
    username = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        # db_table = 'comment'
        # managed = False
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'


class New(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    heading_uz = models.CharField(max_length=500)
    heading_ru = models.CharField(max_length=500)
    heading_en = models.CharField(max_length=500, null=True, blank=True)
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.heading_uz}'

    class Meta:
        verbose_name =  'Новости'
        verbose_name_plural = 'Новости'
