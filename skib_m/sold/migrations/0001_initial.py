# Generated by Django 5.0.1 on 2024-02-04 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Тип оплаты')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('provider_requi', models.CharField(max_length=255, verbose_name='Реквизиты Поставщика')),
            ],
            options={
                'verbose_name': 'Тип оплаты',
                'verbose_name_plural': 'Типы оплаты',
            },
        ),
        migrations.CreateModel(
            name='Type_pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Тип оплаты')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Тип оплаты',
                'verbose_name_plural': 'Типы оплаты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('buyer_name', models.CharField(max_length=255, verbose_name='Покупатель')),
                ('buyer_requi', models.CharField(max_length=255, verbose_name='Реквизиты Покупателя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_unopened', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=0, verbose_name='Колличество')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sold.provider', verbose_name='Поставщики')),
                ('t_pay', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sold.type_pay', verbose_name='Типы оплаты')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]