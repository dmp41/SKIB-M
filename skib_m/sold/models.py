from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    buyer_name = models.CharField(max_length=255, verbose_name="Покупатель")
    buyer_requi = models.CharField(max_length=255, verbose_name="Реквизиты Покупателя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_unopened = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0, verbose_name='Колличество')
    price = models.IntegerField(default=0, verbose_name='Цена')
    t_pay = models.ForeignKey('Type_pay', on_delete=models.PROTECT, verbose_name="Типы оплаты")
    provider = models.ForeignKey('Provider', on_delete=models.PROTECT, verbose_name="Поставщики")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
#        ordering = ['id']

class Type_pay(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Тип оплаты')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type_pay', kwargs={'type_pay_slug': self.slug})

    class Meta:
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'
#        ordering = ['id']

class Provider(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Поставщик')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    provider_requi = models.CharField(max_length=255, verbose_name="Реквизиты Поставщика")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('provider', kwargs={'provider_slug': self.slug})

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
#        ordering = ['id']